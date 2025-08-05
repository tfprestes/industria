# app/routes/maintenance_routes.py

"""
Módulo de rotas para a gestão de Registos de Manutenção.

Define os endpoints para as operações CRUD da entidade 'maintenanceLogs',
que documenta os serviços realizados em ativos e equipamentos de rede.
Integra-se com os módulos de Ativos, Rede, Estoque e o serviço de
armazenamento de ficheiros.
"""

import datetime
import json
import os
from typing import Any, Dict, List, Optional

from firebase_admin import firestore
from flask import (Blueprint, Response, current_app, flash, redirect,
                   render_template, request, session, url_for)
from werkzeug.utils import secure_filename
from werkzeug.wrappers import Response as WerkzeugResponse

from app.auth.routes import login_required, role_required
from app.config import MAINTENANCE_REPAIR_TYPES
from app.services.firestore_service import (add_document, delete_document,
                                            get_all_documents, get_document,
                                            get_documents_by_query,
                                            update_document)
from app.services.storage_service import (delete_file_from_storage,
                                          upload_file_to_storage)

maintenance_bp = Blueprint(
    'maintenance',
    __name__,
    url_prefix='/maintenance'
)


def _get_serviceable_items() -> List[Dict[str, str]]:
    """
    Busca e formata todos os itens que podem receber manutenção.

    Combina 'assets' e 'networkEquipment' numa lista única para ser usada
    em menus de seleção, ordenada alfabeticamente.

    Returns:
        List[Dict[str, str]]: Uma lista de dicionários, cada um com as
                                chaves 'value' (ex: 'assets:id') e 'name'.
    """
    items: List[Dict[str, str]] = []
    try:
        assets = get_all_documents('assets')
        for asset in assets:
            items.append({
                'value': f"assets:{asset['id']}",
                'name': f"Ativo: {asset.get('brand', '')} {asset.get('model', '')} (S/N: {asset.get('serialNumber', 'N/A')})"
            })
        network_equipment = get_all_documents('networkEquipment')
        for eq in network_equipment:
            items.append({
                'value': f"networkEquipment:{eq['id']}",
                'name': f"Rede: {eq.get('brand', '')} {eq.get('model', '')} (IP: {eq.get('ipAddress', 'N/A')})"
            })
    except Exception as e:
        current_app.logger.error(f"Erro ao buscar itens para manutenção: {e}", exc_info=True)
    
    return sorted(items, key=lambda x: x['name'])


@maintenance_bp.route('/')
@login_required
@role_required('admin', 'viewer')
def list_maintenance_logs() -> str:
    """Exibe a lista de todos os registos de manutenção."""
    try:
        maintenance_logs: List[Dict[str, Any]] = get_all_documents('maintenanceLogs')
        items_map: Dict[str, str] = {item['value']: item['name'] for item in _get_serviceable_items()}
        
        for log in maintenance_logs:
            log_entity_key = f"{log.get('entityType')}:{log.get('entityId')}"
            log['entityName'] = items_map.get(log_entity_key, 'Item não encontrado ou excluído')
            if 'logDate' in log and hasattr(log.get('logDate'), 'strftime'):
                log['logDateFormatted'] = log['logDate'].strftime('%d/%m/%Y')

        return render_template('maintenance/list.html', maintenance_logs=maintenance_logs)
    except Exception as e:
        current_app.logger.error(f"Erro ao listar registos de manutenção: {e}", exc_info=True)
        flash("Ocorreu um erro ao carregar os registos de manutenção.", "danger")
        return render_template('maintenance/list.html', maintenance_logs=[])


@maintenance_bp.route('/form', methods=['GET'])
@maintenance_bp.route('/form/<string:log_id>', methods=['GET'])
@login_required
@role_required('admin')
def maintenance_log_form(log_id: Optional[str] = None) -> str | WerkzeugResponse:
    """Exibe um formulário unificado para adicionar ou editar um registo de manutenção."""
    try:
        log: Dict[str, Any] = get_document('maintenanceLogs', log_id) if log_id else {}
        if log_id and not log:
            flash('Registo de manutenção não encontrado.', 'danger')
            return redirect(url_for('maintenance.list_maintenance_logs'))
        
        context: Dict[str, Any] = {
            'log': log,
            'serviceable_items': _get_serviceable_items(),
            'repair_types': MAINTENANCE_REPAIR_TYPES,
            'inventory_items': get_all_documents('inventory')
        }
        return render_template('maintenance/form.html', **context)
    except Exception as e:
        current_app.logger.error(f"Erro ao carregar formulário de manutenção: {e}", exc_info=True)
        flash("Ocorreu um erro ao carregar o formulário.", "danger")
        return redirect(url_for('maintenance.list_maintenance_logs'))


@maintenance_bp.route('/save/', methods=['POST'])
@maintenance_bp.route('/save/<string:log_id>', methods=['POST'])
@login_required
@role_required('admin')
def save_maintenance_log(log_id: Optional[str] = None) -> WerkzeugResponse:
    """Processa a submissão de um registo de manutenção, incluindo peças e upload de anexos."""
    try:
        form_data: Dict[str, Any] = request.form
        required_fields = ['entity', 'log_date', 'description', 'repair_type', 'cost']
        if not all(form_data.get(f) for f in required_fields):
            flash('Todos os campos obrigatórios (*) devem ser preenchidos.', 'danger')
            # Lógica para re-renderizar o formulário com os dados inseridos
            context = {
                'log': dict(form_data), 'serviceable_items': _get_serviceable_items(),
                'repair_types': MAINTENANCE_REPAIR_TYPES, 'inventory_items': get_all_documents('inventory')
            }
            return render_template('maintenance/form.html', **context)

        # --- Lógica de Upload de Anexos ---
        uploaded_files_info: List[Dict[str, Any]] = []
        for file in request.files.getlist("attachment_files"):
            if file and file.filename:
                uploaded_file_data = upload_file_to_storage(file, "maintenanceLogs")
                if uploaded_file_data:
                    uploaded_files_info.append(uploaded_file_data)
                else:
                    flash(f"Tipo de ficheiro não permitido para: {file.filename}", "warning")

        # --- Construção dos dados para salvar ---
        entity_type, entity_id = form_data.get('entity').split(':', 1)
        
        data_to_save: Dict[str, Any] = {
            'entityId': entity_id,
            'entityType': entity_type,
            'logDate': datetime.datetime.strptime(form_data.get('log_date'), '%Y-%m-%d'),
            'description': form_data.get('description'),
            'cost': float(form_data.get('cost', 0)),
            'repairType': form_data.get('repair_type'),
            'partsUsed': json.loads(form_data.get('parts_used_json', '[]')),
        }
        
        technician = form_data.get('technician')
        if technician:
            data_to_save['technician'] = technician
        elif log_id:
            data_to_save['technician'] = firestore.DELETE_FIELD
        
        # Junta anexos antigos (se houver) com os novos
        existing_attachments = json.loads(form_data.get('existing_attachments_json', '[]'))
        data_to_save['attachments'] = existing_attachments + uploaded_files_info

        if log_id:
            update_document('maintenanceLogs', log_id, data_to_save)
            flash('Registo de manutenção atualizado com sucesso!', 'success')
        else:
            add_document('maintenanceLogs', data_to_save)
            flash('Registo de manutenção criado com sucesso!', 'success')

    except Exception as e:
        current_app.logger.error(f"Erro ao salvar registo de manutenção: {e}", exc_info=True)
        flash(f'Ocorreu um erro inesperado ao salvar o registo: {e}', 'danger')
    
    return redirect(url_for('maintenance.list_maintenance_logs'))


@maintenance_bp.route('/delete/<string:log_id>', methods=['POST'])
@login_required
@role_required('admin')
def delete_maintenance_log(log_id: str) -> WerkzeugResponse:
    """Exclui um registo de manutenção e os seus anexos no Storage."""
    try:
        log = get_document('maintenanceLogs', log_id)
        if log:
            for att in log.get('attachments', []):
                if att.get('filePath'):
                    delete_file_from_storage(att['filePath'])
            
            delete_document('maintenanceLogs', log_id)
            flash('Registo de manutenção excluído com sucesso!', 'success')
        else:
            flash('Registo de manutenção não encontrado.', 'danger')
    except Exception as e:
        current_app.logger.error(f"Erro ao excluir registo de manutenção {log_id}: {e}", exc_info=True)
        flash(f'Erro ao excluir registo: {e}', 'danger')
        
    return redirect(url_for('maintenance.list_maintenance_logs'))