# app/config.py
import os

# ======================================================================
# --- Configurações Gerais da Aplicação ---
# ======================================================================
APP_NAME = "ConnectIT"
APP_VERSION = "1.0.0"
ADMIN_ROLE = "admin"
VIEWER_ROLE = "viewer"


# ======================================================================
# --- Chaves Secretas e Credenciais (Carregadas do .env) ---
# ======================================================================
# Chave secreta para segurança da sessão
SECRET_KEY = os.getenv('FLASK_SECRET_KEY', 'uma-chave-super-secreta-para-desenvolvimento')

# Caminho para o arquivo de credenciais do Firebase
FIREBASE_CREDENTIALS_PATH = os.getenv('FIREBASE_CREDENTIALS_PATH')


# ======================================================================
# --- Configurações de Upload de Ficheiros ---
# ======================================================================
# Define o caminho absoluto para a pasta de uploads dentro de 'app/static/'
# Usar os.path.join torna o caminho compatível com qualquer sistema operativo.
UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', 'uploads')

# Define as extensões de ficheiro permitidas para o upload
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'pdf'}


# ======================================================================
# --- Constantes para o Módulo de Ativos ---
# ======================================================================
ASSET_TYPES = {
    'CELULAR': 'celular',
    'COMPUTADOR': 'computador',
    'IMPRESSORA': 'impressora',
    'LICENCA': 'licenca',
}

ASSET_STATUS = ['Ativo', 'Desativado', 'Em Manutenção', 'Excluído']

# Marcas gerais para ativos. Podem ser expandidas conforme necessário.
ASSET_BRANDS = ['Dell', 'Samsung', 'HP', 'Lenovo', 'Apple']

CONTRACT_DURATIONS_MONTHS = [12, 24, 36, 48, 60]


# ======================================================================
# --- Constantes para o Módulo de Despesas ---
# ======================================================================
# Adicionando EXPENSE_TYPES para resolver o ImportError
EXPENSE_TYPES = [
    'Telefonia',
    'Email',
    'Software',
    'Outra'
]


# ======================================================================
# --- Constantes para o Módulo de Infraestrutura de Rede ---
# ======================================================================
NETWORK_EQUIPMENT_TYPES = [
    'Rack',
    'Switch',
    'Câmera UniFi',
    'Controlador de Acesso',
    'Outro'
]

# Dicionário de marcas específicas por tipo de equipamento.
NETWORK_EQUIPMENT_BRANDS = {
    'Switch': ['Huawei', 'TP-Link', 'Dell'],
    'Câmera UniFi': ['UniFi'],
    'Controlador de Acesso': ['Control ID'],
    'Outro': []
}

# Dicionário para categorias de rede, associando a sigla ao nome completo.
NETWORK_CATEGORIES = {
    'TI': 'Tecnologia da Informação',
    'TA': 'Tecnologia da Automação'
}


# ======================================================================
# --- Constantes para o Módulo de Estoque e Manutenção ---
# ======================================================================
INVENTORY_ITEM_TYPES = [
    'Componente',    # (ex: memória RAM, HD/SSD)
    'Consumível',    # (ex: toner, tinteiro, papel)
    'Cabo',          # (ex: cabo de rede, cabo de força)
    'Periférico',    # (ex: rato, teclado)
    'Outro'
]

INVENTORY_UNITS_OF_MEASURE = [
    'Unidade(s)',
    'Caixa(s)',
    'Metro(s)',
    'Rolo(s)'
]

MAINTENANCE_REPAIR_TYPES = [
    'Preventiva',
    'Corretiva',
    'Instalação',
    'Orçamento',
    'Outro'
]