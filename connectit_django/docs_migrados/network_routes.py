# app/routes/network_routes.py

import json
from typing import Any, Dict, List, Optional, Union

from firebase_admin import firestore
from flask import (Blueprint, Response, current_app, flash, redirect,
                   render_template, request, url_for)
from werkzeug.wrappers import Response as WerkzeugResponse

from app.auth.routes import login_required, role_required
from app.config import (ALLOWED_EXTENSIONS, NETWORK_CATEGORIES,
                        NETWORK_EQUIPMENT_BRANDS, NETWORK_EQUIPMENT_TYPES)
from app.models.network_equipment import NetworkEquipment, Port
from app.services.firestore_service import (add_document, delete_document,
                                            get_all_documents, get_document,
                                            update_document)
from app.services.storage_service import (delete_file_from_storage,
                                          upload_file_to_storage)

network_bp = Blueprint(
    'network',
    __name__,
    url_prefix='/network'
)


def _build_network_context(item_data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    item_data = item_data or {}
    try:
        return {
            'equipment': item_data,
            'sectors': get_all_documents('sectors'),
            'units': get_all_documents('units'),
            'cost_centers': get_all_documents('costCenters'),
            'equipment_types': NETWORK_EQUIPMENT_TYPES,
            'equipment_brands': NETWORK_EQUIPMENT_BRANDS,
            'network_categories': NETWORK_CATEGORIES
        }
    except Exception as e:
        current_app.logger.error(f"Erro ao construir contexto para equipamentos de rede: {e}")
        flash("Falha ao carregar dados de apoio.", "warning")
        return {'equipment': item_data}


@network_bp.route('/')
@login_required
@role_required('admin', 'viewer')
def list_network_equipment() -> str:
    try:
        all_equipment: List[Dict[str, Any]] = get_all_documents('networkEquipment')
        sectors_map: Dict[str, str] = {s['id']: s.get('name', 'N/A') for s in get_all_documents('sectors')}
        for eq in all_equipment:
            eq['sectorName'] = sectors_map.get(eq.get('assignedSectorId'), 'N/A')
        return render_template('network/list.html', equipment_list=all_equipment)
    except Exception as e:
        current_app.logger.error(f"Erro ao listar equipamentos de rede: {e}", exc_info=True)
        flash("Ocorreu um erro ao carregar os equipamentos de rede.", "danger")
        return render_template('network/list.html', equipment_list=[])


@network_bp.route('/form', methods=['GET'])
@network_bp.route('/form/<string:equipment_id>', methods=['GET'])
@login_required
@role_required('admin')
def network_equipment_form(equipment_id: Optional[str] = None) -> Union[str, WerkzeugResponse]:
    try:
        equipment: Dict[str, Any] = get_document('networkEquipment', equipment_id) if equipment_id else {}
        if equipment_id and not equipment:
            flash('Equipamento de rede não encontrado.', 'danger')
            return redirect(url_for('network.list_network_equipment'))

        context = _build_network_context(equipment)
        context['equipment_id'] = equipment_id
        return render_template('network/form.html', **context)
    except Exception as e:
        current_app.logger.error(f"Erro ao carregar formulário de rede: {e}", exc_info=True)
        flash("Ocorreu um erro ao carregar o formulário.", "danger")
        return redirect(url_for('network.list_network_equipment'))


@network_bp.route('/save/', methods=['POST'])
@network_bp.route('/save/<string:equipment_id>', methods=['POST'])
@login_required
@role_required('admin')
def save_network_equipment(equipment_id: Optional[str] = None) -> WerkzeugResponse:
    try:
        form_data: Dict[str, Any] = request.form
        required_fields = ['type', 'brand', 'model', 'ip_address', 'network_category', 'assigned_sector_id']
        
        if not all(form_data.get(f) for f in required_fields):
            flash('Todos os campos obrigatórios (*) devem ser preenchidos.', 'danger')
            return redirect(request.referrer or url_for('network.network_equipment_form', equipment_id=equipment_id))

        uploaded_files_info: List[Dict[str, Any]] = [
            upload_file_to_storage(file, "networkEquipment")
            for file in request.files.getlist("attachment_files")
            if file and file.filename and allowed_file(file.filename)
        ]
        
        ports_list: List[Port] = []
        if form_data.get('type') == 'Switch':
            ports_json_str = form_data.get('ports_json', '[]')
            ports_data = json.loads(ports_json_str)
            for port_dict in ports_data:
                port_dict['number'] = int(port_dict['number'])
                port_dict['poe_status'] = port_dict.get('poe_status') == 'on'
                ports_list.append(Port(**port_dict))
        
        existing_attachments = json.loads(form_data.get('existing_attachments_json', '[]'))
        all_attachments = existing_attachments + uploaded_files_info

        equipment_obj = NetworkEquipment(
            id=equipment_id,
            equipment_type=form_data.get('type'),
            brand=form_data.get('brand'),
            model=form_data.get('model'),
            ip_address=form_data.get('ip_address'),
            firmware_version=form_data.get('firmware_version'),
            sector_id=form_data.get('assigned_sector_id'),
            location_description=form_data.get('location_description'),
            network_category=form_data.get('network_category'),
            ports=ports_list,
            attachments=all_attachments
        )
        data_to_save = equipment_obj.to_dict()

        if equipment_id:
            update_document('networkEquipment', equipment_id, data_to_save)
            flash('Equipamento de rede atualizado com sucesso!', 'success')
        else:
            add_document('networkEquipment', data_to_save)
            flash('Equipamento de rede registrado com sucesso!', 'success')

    except Exception as e:
        current_app.logger.error(f"Erro ao salvar equipamento de rede: {e}", exc_info=True)
        flash('Ocorreu um erro inesperado ao salvar o equipamento.', 'danger')
    
    return redirect(url_for('network.list_network_equipment'))


@network_bp.route('/delete/<string:equipment_id>', methods=['POST'])
@login_required
@role_required('admin')
def delete_network_equipment(equipment_id: str) -> WerkzeugResponse:
    try:
        equipment = get_document('networkEquipment', equipment_id)
        if equipment:
            for attachment in equipment.get('attachments', []):
                if 'filePath' in attachment:
                    delete_file_from_storage(attachment['filePath'])
            
            delete_document('networkEquipment', equipment_id)
            flash(f'Equipamento "{equipment.get("brand")} {equipment.get("model")}" e seus anexos foram excluídos.', 'success')
        else:
            flash('Equipamento não encontrado.', 'danger')
    except Exception as e:
        current_app.logger.error(f"Erro ao excluir equipamento de rede {equipment_id}: {e}", exc_info=True)
        flash('Erro ao excluir o equipamento.', 'danger')
        
    return redirect(url_for('network.list_network_equipment'))