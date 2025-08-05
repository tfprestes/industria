# app/services/csv_service.py
import pandas as pd

def export_to_csv(data, filename="export.csv"):
    """Exporta uma lista de dicionários para um arquivo CSV."""
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False, sep=';')
    return filename

def import_from_csv(filename):
    """Importa dados de um arquivo CSV para uma lista de dicionários."""
    try:
        df = pd.read_csv(filename, sep=';')
        return df.to_dict(orient='records')
    except FileNotFoundError:
        print(f"Erro: Arquivo '{filename}' não encontrado.")
        return None
    except Exception as e:
        print(f"Erro ao importar CSV: {e}")
        return None
