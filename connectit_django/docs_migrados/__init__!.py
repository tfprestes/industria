# app/__init__.py

"""
Ponto de entrada principal e fábrica da aplicação Flask (Application Factory).

Este ficheiro é responsável por:
1. Criar e configurar a instância da aplicação Flask.
2. Inicializar serviços essenciais, como o Firebase Admin SDK.
3. Importar e registar todos os blueprints (módulos) da aplicação.
4. Injetar dados globais nos contextos dos templates.
"""

import datetime
import os
from typing import Any, Dict, Optional, Union

import firebase_admin
from firebase_admin import credentials, initialize_app
from flask import Flask, Response 
from werkzeug.wrappers import Response as WerkzeugResponse


def create_app() -> Flask:
    """
    Cria, configura e retorna a instância principal da aplicação Flask.
    """
    app = Flask(__name__)
    app.config.from_object('app.config')

    # --- Inicialização do Firebase Admin SDK ---
    if not firebase_admin._apps:
        cred_path: Optional[str] = app.config.get('FIREBASE_CREDENTIALS_PATH')
        storage_bucket: Optional[str] = app.config.get('FIREBASE_STORAGE_BUCKET')

        if cred_path and os.path.exists(cred_path):
            try:
                cred = credentials.Certificate(cred_path)
                initialize_app(cred, {'storageBucket': storage_bucket})
                app.logger.info("Firebase Admin SDK inicializado com sucesso, incluindo Storage Bucket.")
            except Exception as e:
                app.logger.critical(
                    f"ERRO CRÍTICO: Falha ao inicializar Firebase Admin SDK: {e}",
                    exc_info=True
                )
                raise
        else:
            app.logger.warning("AVISO: 'FIREBASE_CREDENTIALS_PATH' não definida no ambiente/configuração ou arquivo não encontrado.")

    # --- Importação dos Blueprints (Todos os existentes foram mantidos) ---
    from app.auth.routes import auth_bp
    from app.routes.dashboard_routes import dashboard_bp
    from app.routes.asset_routes import asset_bp
    from app.routes.expense_routes import expense_bp
    from app.routes.ticket_metric_routes import ticket_metrics_bp
    from app.routes.network_routes import network_bp
    from app.routes.inventory_routes import inventory_bp
    from app.routes.maintenance_routes import maintenance_bp
    from app.routes.extension_routes import extension_bp
    
    # --- ADIÇÃO SEGURA DO NOVO MÓDULO DE CONTRATOS ---
    from app.routes.contract_routes import contract_bp

    # Módulos de Cadastros Mestres (Intactos)
    from app.routes.sector_routes import sector_bp
    from app.routes.unit_routes import unit_bp
    from app.routes.cost_center_routes import cost_center_bp
    from app.routes.supplier_routes import supplier_bp
    from app.routes.expense_type_routes import expense_type_bp
    from app.routes.asset_type_routes import asset_type_bp

    # --- Registo dos Blueprints na Aplicação (Todos os existentes foram mantidos) ---
    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(asset_bp)
    app.register_blueprint(expense_bp)
    app.register_blueprint(ticket_metrics_bp)
    app.register_blueprint(network_bp)
    app.register_blueprint(inventory_bp)
    app.register_blueprint(maintenance_bp)
    app.register_blueprint(extension_bp)

    # --- REGISTO SEGURO DO NOVO MÓDULO DE CONTRATOS ---
    app.register_blueprint(contract_bp)
    
    # Registos dos Módulos de Cadastros Mestres (Intactos)
    app.register_blueprint(sector_bp)
    app.register_blueprint(unit_bp)
    app.register_blueprint(cost_center_bp)
    app.register_blueprint(supplier_bp)
    app.register_blueprint(expense_type_bp)
    app.register_blueprint(asset_type_bp)

    # --- Processadores de Contexto Globais (Intactos) ---
    @app.context_processor
    def inject_global_data() -> Dict[str, Union[str, int]]:
        """
        Disponibiliza variáveis globais para todos os templates Jinja2.
        """
        return {
            'APP_NAME': app.config.get('APP_NAME', 'ConnectIT'),
            'current_year': datetime.datetime.now().year
        }

    return app