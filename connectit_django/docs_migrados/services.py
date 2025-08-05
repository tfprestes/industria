# app/auth/services.py
from firebase_admin import auth, firestore
from firebase_admin.exceptions import FirebaseError

# Inicializa o cliente do Firestore (será usado para armazenar roles)
# Certifique-se de que firebase_admin.initialize_app() foi chamado em app/__init__.py
try:
    db = firestore.client()
except ValueError:
    # Se o app ainda não foi inicializado, tentamos inicializar (caso seja testado isoladamente)
    # Em um app Flask rodando, initialize_app() já deve ter sido chamado.
    import firebase_admin
    if not firebase_admin._apps:
        # AVISO: Em um ambiente de produção Flask, a inicialização deve ocorrer
        # apenas uma vez em app/__init__.py para evitar problemas.
        # Este bloco é um fallback para teste de módulo isolado.
        print("Aviso: Firebase não inicializado em services.py. Tentando inicializar...")
        # Você precisaria de credenciais aqui para uma inicialização standalone
        # from firebase_admin import credentials
        # cred = credentials.Certificate("path/to/your/firebase-adminsdk.json")
        # firebase_admin.initialize_app(cred)
        # db = firestore.client()
        print("Firebase não pode ser inicializado de forma segura em services.py sem credenciais.")


def register_user(email, password, role='viewer'):
    """
    Regista um novo utilizador no Firebase Authentication e armazena a role no Firestore.

    Args:
        email (str): O email do utilizador.
        password (str): A senha do utilizador.
        role (str, optional): A role do utilizador ('admin' ou 'viewer'). Padrão para 'viewer'.

    Returns:
        tuple: (True, user_id) se o registo for bem-sucedido, (False, erro_mensagem) caso contrário.
    """
    try:
        # Cria o utilizador no Firebase Authentication
        user = auth.create_user(email=email, password=password)
        
        # Armazena a role do utilizador no Firestore
        user_ref = db.collection('users').document(user.uid)
        user_ref.set({'email': email, 'role': role})
        
        print(f"Utilizador {email} registado com sucesso com UID: {user.uid} e role: {role}")
        return True, user.uid
    except FirebaseError as e:
        print(f"Erro ao registar utilizador: {e}")
        return False, str(e)
    except Exception as e:
        print(f"Erro inesperado ao registar utilizador: {e}")
        return False, "Erro inesperado ao registar utilizador."


def authenticate_user(email, password):
    """
    Tenta autenticar um utilizador.

    AVISO DE SEGURANÇA: Num ambiente de produção, a verificação da palavra-passe
    contra o Firebase Authentication deve ocorrer no lado do cliente (com JavaScript do Firebase SDK)
    e o token de ID resultante deve ser enviado para o servidor para verificação.
    Esta implementação serve para demonstração no backend do Flask, mas NÃO É SEGURA
    para verificar diretamente a palavra-passe enviada de um formulário contra o Firebase Auth
    sem um token de ID do cliente.
    Aqui, apenas verificamos se o utilizador existe no Firebase Auth.
    """
    try:
        # Tenta obter o utilizador pelo email.
        # Isto confirma que o utilizador existe no Firebase Auth.
        # NOTA: Isto NÃO verifica a palavra-passe directamente aqui no servidor.
        # Para isso, uma abordagem mais robusta envolve o client-side SDK.
        user = auth.get_user_by_email(email)
        
        # Para fins de desenvolvimento e demonstração, se o utilizador existe,
        # vamos 'assumir' autenticação bem-sucedida e buscar os seus dados e role do Firestore.
        user_data = get_user_data(user.uid)
        if user_data:
            print(f"Utilizador {email} autenticado (via existência) com sucesso. Role: {user_data.get('role')}")
            return True, user_data
        else:
            print(f"Erro: Dados do utilizador {email} não encontrados no Firestore.")
            return False, "Dados do utilizador não encontrados."
            
    except auth.UserNotFoundError:
        print(f"Tentativa de autenticação falhou: Utilizador com email '{email}' não encontrado.")
        return False, "Utilizador ou palavra-passe inválidos."
    except FirebaseError as e:
        print(f"Erro do Firebase ao autenticar utilizador: {e}")
        return False, "Erro na autenticação do Firebase."
    except Exception as e:
        print(f"Erro inesperado ao autenticar utilizador: {e}")
        return False, "Erro inesperado na autenticação."


def get_user_data(uid):
    """
    Busca os dados de um utilizador (incluindo a role) do Firestore.

    Args:
        uid (str): O UID do utilizador.

    Returns:
        dict: Um dicionário com os dados do utilizador, ou None se não encontrado.
    """
    try:
        user_ref = db.collection('users').document(uid)
        user_doc = user_ref.get()
        if user_doc.exists:
            return {'uid': user_doc.id, **user_doc.to_dict()}
        return None
    except Exception as e:
        print(f"Erro ao buscar dados do utilizador {uid} no Firestore: {e}")
        return None

