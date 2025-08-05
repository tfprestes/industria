# ConnectIT

## Gerenciador de Ativos e Despesas

Este é o repositório para a aplicação web ConnectIT, projetada para otimizar o controle financeiro e logístico de ativos de TI e infraestrutura de rede.

### Instalação

1.  **Clone o repositório:**
    `git clone <URL_DO_SEU_REPOSITORIO>`
    `cd connectit`

2.  **Crie e ative um ambiente virtual:**
    `python -m venv venv`
    `source venv/bin/activate` (Linux/macOS)
    `venv\Scripts\activate` (Windows)

3.  **Instale as dependências:**
    `pip install -r requirements.txt`

4.  **Configure as variáveis de ambiente:**
    Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:
    ```
    FIREBASE_API_KEY='sua_chave_api_firebase'
    FLASK_SECRET_KEY='uma_chave_secreta_longa_e_aleatoria'
    # Outras variáveis de configuração do Firebase...
    ```

5.  **Execute a aplicação:**
    `python run.py`

### Estrutura do Projeto

Consulte a documentação completa do escopo para detalhes da estrutura e funcionalidades.
