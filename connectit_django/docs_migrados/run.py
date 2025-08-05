# Ponto de entrada principal da aplicação Flask
import os
from dotenv import load_dotenv

# Define o diretório base do projeto (onde run.py está localizado)
BASEDIR = os.path.abspath(os.path.dirname(__file__))

# Carrega as variáveis de ambiente do arquivo .env
# Isso garante que o .env seja encontrado independentemente de onde o script é executado
load_dotenv(os.path.join(BASEDIR, '.env'))

from app import create_app

app = create_app()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
