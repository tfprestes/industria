# project_analyzer_v2.py
import os
from pathlib import Path
import json

# --- Configurações ---
PROJECT_ROOT = Path.cwd() 

EXCLUDE_DIRS = {
    "__pycache__", ".git", ".idea", ".vscode", "venv", ".venv",
    "env", "node_modules", "static", "media",
}

DJANGO_APP_FILES = [
    "models.py", "views.py", "admin.py", "urls.py", 
    "serializers.py", "tests.py", "forms.py", "services.py",
    "managers.py", "selectors.py"
]

def count_lines_of_code(filepath: Path) -> int:
    """Conta as linhas não vazias de um arquivo de texto."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return sum(1 for line in f if line.strip())
    except (IOError, UnicodeDecodeError):
        return 0

def analyze_django_project(root: Path):
    """
    Analisa uma estrutura de projeto Django, identificando o projeto principal,
    os apps e fornecendo métricas sobre eles.
    """
    if not root.is_dir():
        print(f"ERRO: O diretório '{root}' não foi encontrado.")
        return

    report = {
        "project_root": str(root),
        "django_project_dir": None,
        "django_apps": {},
        "potential_issues": [],
    }

    print(f"Iniciando análise do projeto em: {root}\n")

    # Encontrar o diretório principal do projeto (que contém settings.py)
    settings_files = list(root.rglob("settings.py"))
    for settings_file in settings_files:
        if not any(excluded in settings_file.parts for excluded in EXCLUDE_DIRS):
            report["django_project_dir"] = str(settings_file.parent)
            break
            
    if not report["django_project_dir"]:
        report["potential_issues"].append(
            "Não foi possível localizar 'settings.py'. Verifique se é um projeto Django."
        )
    else:
        print(f"Diretório de configuração Django encontrado: {report['django_project_dir']}")

    # =========================================================================
    #  MELHORIA V2: Lógica de descoberta de Apps recursiva
    #  Agora procuramos por 'apps.py' em qualquer subdiretório.
    # =========================================================================
    app_config_files = list(root.rglob("apps.py"))
    if not app_config_files:
        report["potential_issues"].append("Nenhum arquivo 'apps.py' encontrado. Não foi possível identificar os apps Django.")
    
    for app_config_path in app_config_files:
        # Ignora apps em pastas excluídas (ex: venv)
        if any(excluded in app_config_path.parts for excluded in EXCLUDE_DIRS):
            continue

        path_object = app_config_path.parent  # O diretório do app é o pai de apps.py
        app_name = path_object.name
        
        print(f"Analisando App: {app_name}...")
        report["django_apps"][app_name] = {
            "path": str(path_object),
            "files_of_interest": {},
            "total_loc": 0, # Lines of Code
        }

        app_loc = 0
        for file_path in path_object.rglob("*.py"):
            # Garante que estamos analisando apenas arquivos .py do app e não de sub-apps
            if file_path.parent != path_object and not str(file_path.parent).startswith(str(path_object)):
                 continue

            if file_path.name in DJANGO_APP_FILES:
                loc = count_lines_of_code(file_path)
                report["django_apps"][app_name]["files_of_interest"][file_path.name] = {
                    "path": str(file_path),
                    "loc": loc
                }
            
            app_loc += count_lines_of_code(file_path)

        report["django_apps"][app_name]["total_loc"] = app_loc
        if not (path_object / "tests.py").exists() and not (path_object / "tests").is_dir():
            report["potential_issues"].append(f"O app '{app_name}' não possui um arquivo/diretório de testes ('tests.py' ou 'tests/').")
    
    print("\nAnálise concluída.")
    return report

def print_report(report: dict):
    """Imprime o relatório de análise de forma legível."""
    print("\n" + "="*80)
    print("           RELATÓRIO DE ANÁLISE DO PROJETO DJANGO (v2)")
    print("="*80)

    if report.get("django_project_dir"):
        print(f"\nDiretório de Configuração do Projeto:\n  {report['django_project_dir']}")
    
    print("\n--- Django Apps Identificados ---")
    if not report["django_apps"]:
        print("  Nenhum app Django foi identificado.")
    else:
        sorted_apps = sorted(
            report["django_apps"].items(), 
            key=lambda item: item[1]['total_loc'], 
            reverse=True
        )
        for app_name, app_data in sorted_apps:
            print(f"\n  [APP] {app_name} (Total de ~{app_data['total_loc']} linhas de código Python)")
            
            sorted_files = sorted(
                app_data['files_of_interest'].items(),
                key=lambda item: item[1]['loc'],
                reverse=True
            )
            for file_name, file_data in sorted_files:
                print(f"    - {file_name:<20} | LOC: {file_data['loc']}")

    if report["potential_issues"]:
        print("\n--- Pontos de Atenção (Potential Issues) ---")
        for issue in report["potential_issues"]:
            print(f"  - [AVISO] {issue}")

    print("\n" + "="*80)
    print("Sugestão: Inicie a análise pelos apps e arquivos com maior 'LOC' (Lines of Code).")
    print("="*80)

if __name__ == "__main__":
    analysis_result = analyze_django_project(PROJECT_ROOT)
    if analysis_result:
        print_report(analysis_result)
        
        report_file = "project_analysis_report_v2.json"
        with open(report_file, "w", encoding="utf-8") as f:
            json.dump(analysis_result, f, indent=4, ensure_ascii=False)
        print(f"\nRelatório detalhado salvo em '{report_file}'")