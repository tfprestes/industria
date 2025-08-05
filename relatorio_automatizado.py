import os
import re

SENSITIVE_KEYWORDS = [
    "password", "senha", "secret", "token", "api_key", "chave", "confidential",
    "PRIVATE_KEY", "AWS_SECRET", "DATABASE_URL"
]
FILE_EXTS_CODE = ('.py', '.js', '.ts', '.java', '.c', '.cpp', '.rb', '.php')
FILE_EXTS_CONFIG = ('.env', '.ini', '.yml', '.yaml', '.json')

def map_todos(root_path, out_file="todos_report.md"):
    todos = []
    for dirpath, _, filenames in os.walk(root_path):
        for fname in filenames:
            if not fname.endswith(FILE_EXTS_CODE):
                continue
            fp = os.path.join(dirpath, fname)
            try:
                with open(fp, encoding="utf-8", errors="ignore") as f:
                    for i, line in enumerate(f, 1):
                        if re.search(r'\b(TODO|FIXME)\b', line, re.IGNORECASE):
                            # Adiciona contexto (2 linhas antes e depois)
                            context = []
                            f.seek(0)
                            lines = f.readlines()
                            start = max(0, i - 3)
                            end = min(len(lines), i + 2)
                            context = ''.join(lines[start:end]).strip()
                            todos.append((fp, i, line.strip(), context))
                            break  # Só o primeiro TODO/FIXME por arquivo/linha
            except Exception as e:
                continue
    with open(out_file, "w", encoding="utf-8") as f:
        f.write("# TODOs e FIXMEs Encontrados\n\n")
        for file, lineno, text, context in todos:
            f.write(f"---\n- **{file}:{lineno}** — `{text}`\n```\n{context}\n```\n")
    print(f"Relatório gerado: {out_file} (Total: {len(todos)} TODOs/FIXMEs)")

def find_sensitive_info(root_path, out_file="sensitive_report.md"):
    findings = []
    for dirpath, _, filenames in os.walk(root_path):
        for fname in filenames:
            if not fname.endswith(FILE_EXTS_CODE + FILE_EXTS_CONFIG):
                continue
            fp = os.path.join(dirpath, fname)
            try:
                with open(fp, encoding="utf-8", errors="ignore") as f:
                    for i, line in enumerate(f, 1):
                        if any(kw.lower() in line.lower() for kw in SENSITIVE_KEYWORDS):
                            findings.append((fp, i, line.strip()))
            except Exception as e:
                continue
    with open(out_file, "w", encoding="utf-8") as f:
        f.write("# Possíveis informações sensíveis no código\n\n")
        for file, lineno, text in findings:
            f.write(f"---\n- **{file}:{lineno}** — `{text}`\n")
    print(f"Relatório gerado: {out_file} (Total: {len(findings)} achados)")

def largest_files(root_path, out_file="largest_files_report.md", top_n=20):
    files = []
    for dirpath, _, filenames in os.walk(root_path):
        for fname in filenames:
            if not fname.endswith(FILE_EXTS_CODE):
                continue
            fp = os.path.join(dirpath, fname)
            try:
                with open(fp, encoding="utf-8", errors="ignore") as f:
                    content = f.read()
                    lines = content.splitlines()
                    n_funcs = len(re.findall(r'\b(def |function |class )', content))
                    files.append((fp, len(lines), n_funcs))
            except Exception as e:
                continue
    files = sorted(files, key=lambda x: -x[1])[:top_n]
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(f"# Top {top_n} maiores arquivos do projeto\n\n")
        for file, lines, n_funcs in files:
            f.write(f"---\n- **{file}** — {lines} linhas, {n_funcs} funções/classes\n")
    print(f"Relatório gerado: {out_file}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Uso: python relatorio_automatizado.py <caminho_do_projeto>")
        exit(1)
    root_path = sys.argv[1]
    print("Mapeando TODOs/FIXMEs...")
    map_todos(root_path)
    print("Mapeando informações sensíveis...")
    find_sensitive_info(root_path)
    print("Levantando maiores arquivos...")
    largest_files(root_path)
    print("\nPronto! Relatórios gerados na pasta do script.")
