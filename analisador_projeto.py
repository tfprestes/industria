import os
import re
import json
import hashlib
import subprocess
from collections import defaultdict, Counter

SENSITIVE_KEYWORDS = [
    "password", "senha", "secret", "token", "api_key", "chave", "confidential",
    "PRIVATE_KEY", "AWS_SECRET", "DATABASE_URL"
]
DANGEROUS_FUNCTIONS = [
    "eval", "exec", "pickle.loads", "subprocess.Popen", "os.system", "system(", "execfile", "input(", "rm -rf", "curl "
]
DEPRECATED_APIS = [
    "imp ", "Buffer(", "collections.MutableMapping", "apply(", "setDaemon", "assertEquals"
]
CONFIG_EXTS = (".env", ".yml", ".yaml", ".ini", ".cfg", ".conf", ".toml")

IGNORED_DIRS = {'venv', 'node_modules', '.git', 'build', 'dist', '__pycache__', '.idea', '.vscode', '.svn', '.hg', '.tox'}
MAX_FILESIZE = 2 * 1024 * 1024  # 2 MB

def hash_code_block(block):
    return hashlib.md5(block.encode('utf-8')).hexdigest()

def scan_file(file_path):
    try:
        if os.path.getsize(file_path) > MAX_FILESIZE:
            print(f"[SKIP] Arquivo muito grande: {file_path}")
            return None
    except Exception as e:
        print(f"[WARN] Erro ao obter tamanho de {file_path}: {e}")
        return None
    try:
        with open(file_path, encoding='utf-8', errors='ignore') as f:
            content = f.read()
    except Exception as e:
        print(f"[WARN] Erro lendo {file_path}: {e}")
        return None
    lines = content.split('\n')
    ext = os.path.splitext(file_path)[-1].lower()
    num_lines = len(lines)
    num_todos = sum(1 for l in lines if 'TODO' in l or 'FIXME' in l)
    sensitive_hits = [l for l in lines if any(kw in l.lower() for kw in SENSITIVE_KEYWORDS)]
    dangerous_hits = [l for l in lines if any(df in l for df in DANGEROUS_FUNCTIONS)]
    deprecated_hits = [l for l in lines if any(api in l for api in DEPRECATED_APIS)]
    code_blocks = re.findall(r'((?:def |function |class |func |public |private ).{0,200}\{[\s\S]+?\})', content)
    imports = re.findall(r'(?:import|from)\s+([\w\.]+)', content)
    # Para Node.js
    requires = re.findall(r'require\([\'"]([\w\./\-]+)[\'"]\)', content)
    return {
        "path": file_path,
        "ext": ext,
        "lines": num_lines,
        "todos": num_todos,
        "sensitive_hits": sensitive_hits,
        "dangerous_hits": dangerous_hits,
        "deprecated_hits": deprecated_hits,
        "code_blocks": [hash_code_block(cb) for cb in code_blocks],
        "imports": imports + requires,
        "all_imports": imports,
        "content": content,
    }

def walk_project(root_path):
    stats = []
    all_files = []
    for dirpath, dirnames, filenames in os.walk(root_path):
        dirnames[:] = [d for d in dirnames if d not in IGNORED_DIRS]
        for fname in filenames:
            fp = os.path.join(dirpath, fname)
            all_files.append(fp)
            if fp.endswith(('.py', '.js', '.ts', '.java', '.c', '.cpp', '.go', '.rb', '.php', '.cs', '.swift', '.kt', '.rs', '.scala')):
                res = scan_file(fp)
                if res:
                    stats.append(res)
                print(f"[OK] {fp}")
    return stats, all_files

def find_orphans(stats, all_files):
    referenced = set()
    for stat in stats:
        referenced.update([os.path.normpath(os.path.join(os.path.dirname(stat["path"]), imp.replace(".", os.sep) + stat["ext"])) for imp in stat["imports"]])
    orphans = [f for f in all_files if f not in referenced and not os.path.basename(f).startswith('__')]
    return orphans

def find_import_cycles(stats):
    graph = defaultdict(list)
    for stat in stats:
        node = os.path.relpath(stat["path"])
        for imp in stat["imports"]:
            graph[node].append(imp)
    cycles = []
    visited = set()
    def visit(n, stack):
        if n in stack:
            cycles.append(list(stack) + [n])
            return
        if n in visited:
            return
        visited.add(n)
        for neighbor in graph.get(n, []):
            visit(neighbor, stack + [n])
    for node in graph:
        visit(node, [])
    return cycles

def check_vulnerable_dependencies(root_path):
    findings = {}
    # Node.js
    if os.path.exists(os.path.join(root_path, "package.json")):
        try:
            output = subprocess.getoutput(f"cd \"{root_path}\" && npm audit --json")
            audit = json.loads(output)
            if "advisories" in audit and audit["advisories"]:
                findings["node"] = list(audit["advisories"].values())
        except Exception as e:
            findings["node"] = str(e)
    # Python
    if os.path.exists(os.path.join(root_path, "requirements.txt")):
        try:
            output = subprocess.getoutput(f"safety check -r \"{os.path.join(root_path, 'requirements.txt')}\" --json")
            findings["python"] = json.loads(output)
        except Exception as e:
            findings["python"] = str(e)
    return findings

def analyze(stats, all_files, root_path):
    total_lines = sum(s['lines'] for s in stats)
    file_exts = Counter(s['ext'] for s in stats)
    todos = sum(s['todos'] for s in stats)
    sensitive = [hit for s in stats for hit in s['sensitive_hits']]
    dangerous = [hit for s in stats for hit in s['dangerous_hits']]
    deprecated = [hit for s in stats for hit in s['deprecated_hits']]
    blocks = defaultdict(list)
    for s in stats:
        for b in s['code_blocks']:
            blocks[b].append(s['path'])
    duplicates = {h: ps for h, ps in blocks.items() if len(ps) > 1}
    orphans = find_orphans(stats, all_files)
    import_cycles = find_import_cycles(stats)
    vulnerabilities = check_vulnerable_dependencies(root_path)
    config_files = [f for f in all_files if f.endswith(CONFIG_EXTS)]
    largest_files = sorted(stats, key=lambda x: -x['lines'])[:5]
    return {
        "total_files": len(stats),
        "total_lines": total_lines,
        "file_types": dict(file_exts),
        "todos": todos,
        "sensitive_strings": sensitive,
        "dangerous_uses": dangerous,
        "deprecated_uses": deprecated,
        "duplicated_code_blocks": duplicates,
        "orphans": orphans,
        "import_cycles": import_cycles,
        "config_files": config_files,
        "vulnerabilities": vulnerabilities,
        "largest_files": largest_files,
    }

def print_report(analysis):
    print("="*50)
    print("🔍 RELATÓRIO DE ANÁLISE PROFUNDA DE PROJETO")
    print("="*50)
    print(f"Arquivos analisados: {analysis['total_files']}")
    print(f"Linhas totais de código: {analysis['total_lines']}")
    print(f"Tipos de arquivos: {analysis['file_types']}")
    print(f"Maiores arquivos:")
    for f in analysis['largest_files']:
        print(f"  - {f['path']} ({f['lines']} linhas)")
    print(f"TODOs/FIXMEs encontrados: {analysis['todos']}")
    if analysis['sensitive_strings']:
        print("⚠️  Strings sensíveis encontradas:")
        for s in analysis['sensitive_strings']:
            print(f"   {s}")
    if analysis['dangerous_uses']:
        print("⚠️  Uso de funções perigosas encontradas:")
        for s in analysis['dangerous_uses']:
            print(f"   {s}")
    if analysis['deprecated_uses']:
        print("⚠️  Uso de APIs obsoletas/depreciadas:")
        for s in analysis['deprecated_uses']:
            print(f"   {s}")
    if analysis['duplicated_code_blocks']:
        print("⚠️  Blocos de código duplicados (arquivos):")
        for paths in analysis['duplicated_code_blocks'].values():
            print("   - " + ", ".join(paths))
    if analysis['orphans']:
        print("⚠️  Arquivos órfãos (não referenciados):")
        for o in analysis['orphans']:
            print("   - " + o)
    if analysis['import_cycles']:
        print("⚠️  Ciclos de importação/dependência detectados:")
        for c in analysis['import_cycles']:
            print("   -> " + " -> ".join(c))
    if analysis['vulnerabilities']:
        print("⚠️  Vulnerabilidades detectadas em dependências:")
        for k, v in analysis['vulnerabilities'].items():
            print(f"   [{k}]: {v}")
    if analysis['config_files']:
        print(f"Arquivos de configuração encontrados: {analysis['config_files']}")
    print("="*50)
    print("🔧 RECOMENDAÇÕES AVANÇADAS:")
    if analysis['todos'] > 0:
        print("• Resolva todos os TODOs e FIXMEs.")
    if analysis['sensitive_strings']:
        print("• Remova ou oculte strings sensíveis/hardcoded.")
    if analysis['dangerous_uses']:
        print("• Substitua funções perigosas por alternativas seguras.")
    if analysis['deprecated_uses']:
        print("• Atualize usos de APIs depreciadas.")
    if analysis['duplicated_code_blocks']:
        print("• Refatore blocos de código duplicados para evitar manutenção difícil.")
    if analysis['orphans']:
        print("• Avalie remover arquivos órfãos não utilizados.")
    if analysis['import_cycles']:
        print("• Resolva ciclos de dependência para evitar bugs difíceis.")
    if analysis['vulnerabilities']:
        print("• Atualize e corrija dependências vulneráveis.")
    if analysis['config_files']:
        print("• Restrinja permissões de arquivos de configuração e secrets.")
    print("• Considere adicionar testes automatizados e linter/formatter.")
    print("="*50)

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Uso: python analisador_projeto.py <caminho_do_projeto>")
        exit(1)
    root_path = sys.argv[1]
    stats, all_files = walk_project(root_path)
    analysis = analyze(stats, all_files, root_path)
    print_report(analysis)
    # Salva relatório detalhado em JSON e Markdown
    with open("relatorio_projeto_completo.json", "w", encoding="utf-8") as f:
        json.dump(analysis, f, ensure_ascii=False, indent=2)
    with open("relatorio_projeto_completo.md", "w", encoding="utf-8") as f:
        f.write("# Relatório de Análise Profunda de Projeto\n\n")
        for key, val in analysis.items():
            f.write(f"## {key}\n")
            f.write(f"```\n{json.dumps(val, indent=2, ensure_ascii=False)}\n```\n\n")
