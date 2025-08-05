# app/routes/asset_type_routes.py

import csv
import io
import datetime
from typing import Any, Dict, List, Optional, Union

import pandas as pd
from firebase_admin import firestore
from flask import (Blueprint, Response, current_app, flash, redirect,
                   render_template, request, url_for)
from werkzeug.datastructures import FileStorage
from werkzeug.wrappers import Response as WerkzeugResponse

from app.auth.routes import login_required, role_required
from app.config import ALLOWED_EXTENSIONS
from app.models.asset_type import AssetType
# --- CORREÇÃO: Adicionada a importação da função necessária ---
from app.services.firestore_service import (add_document, delete_document,
                                            get_all_documents, get_document,
                                            get_documents_by_query,
                                            get_documents_with_query, # <--- Adicionada para a verificação
                                            update_document)

asset_type_bp = Blueprint(
    'asset_types',
    __name__,
    url_prefix='/asset_types'
)

def allowed_file(filename: str) -> bool:
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@asset_type_bp.route('/')
@login_required
def list_asset_types() -> str:
    """Exibe a lista de todos os Tipos de Ativos."""
    try:
        asset_types = get_all_documents('assetTypes')
        return render_template('settings/asset_types_list.html', asset_types=asset_types)
    except Exception as e:
        current_app.logger.error(f"Erro ao listar tipos de ativos: {e}", exc_info=True)
        flash("Ocorreu um erro ao carregar a lista de tipos de ativo.", "danger")
        return render_template('settings/asset_types_list.html', asset_types=[])


@asset_type_bp.route('/form', methods=['GET'])
@asset_type_bp.route('/form/<string:asset_type_id>', methods=['GET'])
@login_required
@role_required('admin')
def asset_type_form(asset_type_id: Optional[str] = None) -> Union[str, WerkzeugResponse]:
    """Exibe um formulário para adicionar ou editar um Tipo de Ativo."""
    try:
        asset_type = get_document('assetTypes', asset_type_id) if asset_type_id else {}
        if asset_type_id and not asset_type:
            flash('Tipo de Ativo não encontrado.', 'danger')
            return redirect(url_for('asset_types.list_asset_types'))
        return render_template('settings/asset_type_form.html', asset_type=asset_type)
    except Exception as e:
        current_app.logger.error(f"Erro ao carregar formulário de tipo de ativo: {e}", exc_info=True)
        flash("Ocorreu um erro ao carregar o formulário.", "danger")
        return redirect(url_for('asset_types.list_asset_types'))


@asset_type_bp.route('/save/', methods=['POST'])
@asset_type_bp.route('/save/<string:asset_type_id>', methods=['POST'])
@login_required
@role_required('admin')
def save_asset_type(asset_type_id: Optional[str] = None) -> WerkzeugResponse:
    """Processa a submissão para criar ou atualizar um Tipo de Ativo."""
    try:
        form_data = request.form
        name = form_data.get('name')
        if not name or not name.strip():
            flash('O nome do Tipo de Ativo é obrigatório.', 'danger')
            return render_template('settings/asset_type_form.html', asset_type=dict(form_data))

        asset_type_obj = AssetType(
            name=name.strip(),
            description=form_data.get('description', '').strip() or None,
            default_operating_system=form_data.get('default_operating_system', '').strip() or None,
            id=asset_type_id
        )
        data_to_save = asset_type_obj.to_dict()

        if asset_type_id:
            update_document('assetTypes', asset_type_id, data_to_save)
            flash(f'Tipo de Ativo "{data_to_save["name"]}" atualizado com sucesso!', 'success')
        else:
            add_document('assetTypes', data_to_save)
            flash(f'Tipo de Ativo "{data_to_save["name"]}" criado com sucesso!', 'success')
    except Exception as e:
        current_app.logger.error(f"Erro ao salvar tipo de ativo: {e}", exc_info=True)
        flash("Ocorreu um erro inesperado ao salvar o tipo de ativo.", "danger")

    return redirect(url_for('asset_types.list_asset_types'))


@asset_type_bp.route('/delete/<string:asset_type_id>', methods=['POST'])
@login_required
@role_required('admin')
def delete_asset_type(asset_type_id: str) -> WerkzeugResponse:
    """
    Exclui um tipo de ativo, mas antes verifica se ele não está em uso por nenhum ativo.
    """
    try:
        # Passo 1: Verificar se algum ativo está a usar este tipo
        query_params = [{'field': 'assetTypeId', 'op': '==', 'value': asset_type_id}]
        assets_in_use = get_documents_with_query('assets', query_params, limit=1)

        if assets_in_use:
            # Se a lista não estiver vazia, o tipo está em uso, então a exclusão é bloqueada.
            flash('Não é possível excluir este tipo de ativo, pois ele já está em uso por um ou mais ativos.', 'danger')
        else:
            # Se estiver vazia, podemos excluir com segurança.
            asset_type = get_document('assetTypes', asset_type_id)
            type_name = asset_type.get('name', '') if asset_type else asset_type_id

            if delete_document('assetTypes', asset_type_id):
                flash(f'Tipo de Ativo "{type_name}" excluído com sucesso!', 'success')
            else:
                flash('Erro ao tentar excluir o Tipo de Ativo.', 'danger')
    
    except Exception as e:
        current_app.logger.error(f"Erro ao excluir o tipo de ativo {asset_type_id}: {e}", exc_info=True)
        flash("Ocorreu um erro inesperado ao tentar excluir o tipo de ativo.", "danger")

    # Passo 2: SEMPRE redirecionar de volta para a lista, corrigindo o TypeError original.
    return redirect(url_for('asset_types.list_asset_types'))


# --- Rotas de Importação e Exportação ---
# Se você tiver as suas funções de import/export/template aqui,
# elas devem ser mantidas abaixo deste ponto. O código acima não as remove.