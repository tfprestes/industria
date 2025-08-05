# Em: migration_scripts/export_firebase_collections.py

import os
import csv
import firebase_admin
from firebase_admin import credentials, firestore

# --- CONFIGURAÇÃO ---

# 1. Caminho para a sua chave de serviço do Firebase
#    Vá para o Console do Firebase > Configurações do Projeto > Contas de Serviço
#    Clique em "Gerar nova chave privada" e salve o arquivo JSON nesta pasta.
CREDENTIALS_FILE = 'firebase-service-account-key.json' 

# 2. Lista de coleções que queremos exportar
COLLECTIONS_TO_EXPORT = [
    'assetTypes', 'assets', 'contracts', 'costCenters', 'extensions',
    'inventory', 'networkEquipment', 'sectors', 'suppliers',
    'ticketMetrics', 'units', 'users'
]

# 3. Pasta onde os arquivos CSV serão salvos
OUTPUT_FOLDER = 'firebase_export_csv'

# --- FIM DA CONFIGURAÇÃO ---

def export_collection_to_csv(db, collection_name, output_folder):
    """Lê todos os documentos de uma coleção e salva num arquivo CSV."""
    print(f"Exportando coleção: '{collection_name}'...")
    
    docs = db.collection(collection_name).stream()
    
    # Lista para guardar os dados de todos os documentos
    all_rows = []
    # Set para guardar todos os cabeçalhos possíveis
    all_headers = set()

    for doc in docs:
        row = doc.to_dict()
        row['id_firestore'] = doc.id # Adiciona o ID original do documento
        all_rows.append(row)
        all_headers.update(row.keys())

    if not all_rows:
        print(f"Aviso: Coleção '{collection_name}' está vazia ou não foi encontrada.")
        return

    # Garante uma ordem consistente para os cabeçalhos
    ordered_headers = sorted(list(all_headers))
    
    # Cria o arquivo CSV
    output_file = os.path.join(output_folder, f"{collection_name}.csv")
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=ordered_headers)
        writer.writeheader()
        writer.writerows(all_rows)

    print(f"Sucesso! {len(all_rows)} documentos salvos em '{output_file}'")

def main():
    """Função principal para autenticar e iniciar a exportação."""
    if not os.path.exists(CREDENTIALS_FILE):
        print(f"ERRO: Arquivo de credenciais '{CREDENTIALS_FILE}' não encontrado.")
        print("Por favor, baixe a chave da sua conta de serviço do Firebase e coloque-a nesta pasta.")
        return

    # Autenticação com o Firebase
    cred = credentials.Certificate(CREDENTIALS_FILE)
    firebase_admin.initialize_app(cred)
    db = firestore.client()

    # Cria a pasta de saída se não existir
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    # Itera e exporta cada coleção da lista
    for collection in COLLECTIONS_TO_EXPORT:
        export_collection_to_csv(db, collection, OUTPUT_FOLDER)

if __name__ == '__main__':
    main()