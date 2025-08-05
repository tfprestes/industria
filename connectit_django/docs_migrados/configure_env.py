import os
from dotenv import dotenv_values

def configure_env_file():
    """
    Gera uma FLASK_SECRET_KEY aleatória e configura
    FIREBASE_CREDENTIALS_PATH no arquivo .env.
    """
    env_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.env')
    
    # 1. Definir o caminho para as credenciais do Firebase
    #    (Baseado na informação que você forneceu)
    firebase_credentials_full_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'firebase-adminsdk.json').replace('\\', '/')
    print(f"Caminho esperado para as credenciais do Firebase: {firebase_credentials_full_path}")

    # 2. Gerar uma FLASK_SECRET_KEY aleatória e segura
    flask_secret_key = os.urandom(24).hex()
    print(f"Nova FLASK_SECRET_KEY gerada: '{flask_secret_key}'")

    # 3. Ler o conteúdo atual do .env
    env_content = ""
    if os.path.exists(env_path):
        with open(env_path, 'r', encoding='utf-8') as f:
            env_content = f.read()

    lines = env_content.splitlines()
    updated_lines = []
    
    # Flags para verificar se as chaves já existem e foram atualizadas
    firebase_path_updated = False
    flask_key_updated = False

    for line in lines:
        if line.strip().startswith('FIREBASE_CREDENTIALS_PATH='):
            updated_lines.append(f"FIREBASE_CREDENTIALS_PATH={firebase_credentials_full_path}")
            firebase_path_updated = True
        elif line.strip().startswith('FLASK_SECRET_KEY='):
            updated_lines.append(f"FLASK_SECRET_KEY='{flask_secret_key}'")
            flask_key_updated = True
        else:
            updated_lines.append(line)
    
    # Adicionar as chaves se não existirem
    if not firebase_path_updated:
        updated_lines.append(f"FIREBASE_CREDENTIALS_PATH={firebase_credentials_full_path}")
    if not flask_key_updated:
        updated_lines.append(f"FLASK_SECRET_KEY='{flask_secret_key}'")

    # 4. Escrever o conteúdo atualizado de volta no .env
    with open(env_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(updated_lines))

    print(f"\nArquivo .env atualizado com sucesso em: {env_path}")
    print("Verifique o arquivo .env para confirmar as configurações.")

if __name__ == "__main__":
    configure_env_file()
