# app/routes/asset_routes.py

import csv
import datetime
import io
import json
from typing import Any, Dict, List, Optional, Union

import pandas as pd
from firebase_admin import firestore
from flask import (Blueprint, Response, current_app, flash, redirect,
                   render_template, request, session, url_for)
from werkzeug.wrappers import Response as WerkzeugResponse

from app.auth.routes import login_required, role_required
from app.config import ALLOWED_EXTENSIONS, ASSET_BRANDS, ASSET_STATUS
from app.models.asset import Asset
# Importamos a função get_documents_with_query que é mais poderosa
from app.services.firestore_service import (add_document, delete_document,
                                            get_all_documents, get_document,
                                            get_documents_with_query,
                                            update_document)
from app.services.storage_service import (delete_file_from_storage,
                                          upload_file_to_storage)

asset_bp = Blueprint('assets', __name__, url_prefix='/assets')

# --- Funções Auxiliares (Mantidas como estão) ---
def _parse_date(date_string: Optional[str], date_format: str = '%Y-%m-%d') -> Optional[datetime.datetime]:
    if not date_string: return None
    try: return datetime.datetime.strptime(str(date_string).strip(), date_format)
    except (ValueError, TypeError): return None

def _get_form_context(asset_data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    asset_data = asset_data or {}
    return {
        'asset': asset_data, 'sectors': get_all_documents('sectors'),
        'units': get_all_documents('units'), 'cost_centers': get_all_documents('costCenters'),
        'suppliers': get_all_documents('suppliers'), 'asset_types': get_all_documents('assetTypes'),
        'asset_status': ASSET_STATUS, 'asset_brands': ASSET_BRANDS,
    }

def allowed_file(filename: str) -> bool:
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# --- ROTAS PRINCIPAIS ---

@asset_bp.route('/')
@login_required
def list_assets() -> str:
    """
    Exibe a lista de ativos com funcionalidades de filtro, busca e ordenação.
    (Versão Refatorada)
    """
    try:
        sort_by = request.args.get('sort_by', 'brand')
        filter_type = request.args.get('filter_type', '')
        filter_status = request.args.get('filter_status', '')
        search_term = request.args.get('q', '').strip()

        query_filters = []
        if filter_type:
            query_filters.append({'field': 'assetTypeId', 'op': '==', 'value': filter_type})
        if filter_status:
            query_filters.append({'field': 'status', 'op': '==', 'value': filter_status})
        if search_term:
            # Esta busca simples pode ser expandida para outros campos se necessário
            query_filters.append({'field': 'model', 'op': '>=', 'value': search_term})
            query_filters.append({'field': 'model', 'op': '<=', 'value': search_term + u'\uf8ff'})

        assets = get_documents_with_query(
            'assets', query_params=query_filters, order_by=sort_by
        )

        maps = {
            'sectors': {s['id']: s.get('name', 'N/A') for s in get_all_documents('sectors')},
            'assetTypes': {at['id']: at.get('name', 'N/A') for at in get_all_documents('assetTypes')},
            'costCenters': {cc['id']: cc.get('name', 'N/A') for cc in get_all_documents('costCenters')}
        }
        for asset in assets:
            asset['sectorName'] = maps['sectors'].get(asset.get('assignedSectorId'))
            asset['assetTypeName'] = maps['assetTypes'].get(asset.get('assetTypeId'))
            asset['costCenterName'] = maps['costCenters'].get(asset.get('assignedCostCenterId'))

        context = {
            'assets': assets,
            'all_asset_types': get_all_documents('assetTypes'),
            'asset_status_list': ASSET_STATUS,
            'current_filters': {'type': filter_type, 'status': filter_status, 'q': search_term},
            'current_sort': sort_by
        }
        return render_template('assets/list.html', **context)
    except Exception as e:
        if 'requires an index' in str(e):
            flash("A combinação de filtro/busca requer um índice no Firestore. O link para criação está no log do terminal.", "warning")
        else:
            flash("Ocorreu um erro ao carregar a lista de ativos.", "danger")
        current_app.logger.error(f"Erro ao listar ativos: {e}", exc_info=True)
        return render_template('assets/list.html', assets=[], all_asset_types=get_all_documents('assetTypes'), asset_status_list=ASSET_STATUS, current_filters={}, current_sort='brand')

@asset_bp.route('/form', methods=['GET'])
@asset_bp.route('/form/<string:asset_id>', methods=['GET'])
@login_required
@role_required('admin')
def asset_form(asset_id: Optional[str] = None) -> Union[str, WerkzeugResponse]:
    try:
        asset = get_document('assets', asset_id) if asset_id else {}
        if asset_id and not asset:
            flash('Ativo não encontrado.', 'danger')
            return redirect(url_for('assets.list_assets'))
        context = _get_form_context(asset)
        return render_template('assets/form.html', **context)
    except Exception as e:
        current_app.logger.error(f"Erro ao carregar formulário de ativo: {e}", exc_info=True)
        return redirect(url_for('assets.list_assets'))

@asset_bp.route('/save/', methods=['POST'])
@asset_bp.route('/save/<string:asset_id>', methods=['POST'])
@login_required
@role_required('admin')
def save_asset(asset_id: Optional[str] = None) -> WerkzeugResponse:
    """
    Salva um novo ativo ou atualiza um existente, incluindo os campos dinâmicos.
    (Versão Refatorada)
    """
    try:
        form_data = request.form
        required_fields = ['asset_type_id', 'brand', 'model', 'status', 'lease_value', 'lease_date',
                           'assigned_sector_id', 'assigned_unit_id', 'assigned_cost_center_id']
        if not all(form_data.get(f) for f in required_fields):
            flash('Todos os campos obrigatórios (*) devem ser preenchidos.', 'danger')
            return redirect(request.referrer or url_for('assets.list_assets'))

        uploaded_files_info = [upload_file_to_storage(file, "assets") for file in request.files.getlist("attachment_files") if file and file.filename]

        asset_obj = Asset(
            id=asset_id,
            asset_type_id=form_data.get('asset_type_id'), brand=form_data.get('brand'), model=form_data.get('model'),
            status=form_data.get('status'), serial_number=form_data.get('serial_number'),
            lease_value=float(form_data.get('lease_value', 0.0)),
            lease_date=_parse_date(form_data.get('lease_date')),
            assigned_sector_id=form_data.get('assigned_sector_id'), assigned_unit_id=form_data.get('assigned_unit_id'),
            assigned_cost_center_id=form_data.get('assigned_cost_center_id'),
            user=form_data.get('user'), responsible=form_data.get('responsible'),
            description=form_data.get('description'),
            supplier_id=form_data.get('supplier_id'), invoice_number=form_data.get('invoice_number'),
            contract_duration_months=int(form_data.get('contract_duration_months')) if form_data.get('contract_duration_months') else None,
            receipt_date=_parse_date(form_data.get('receipt_date')),
            shared_with=json.loads(form_data.get('shared_with_json', '[]')),
            attachments=json.loads(form_data.get('existing_attachments_json', '[]')) + uploaded_files_info,
            
            # Lendo os novos campos dinâmicos do formulário
            operating_system=form_data.get('operating_system'), processor=form_data.get('processor'),
            memory=form_data.get('memory'), office_version=form_data.get('office_version'),
            ip_address=form_data.get('ip_address'),
            imei=form_data.get('imei'),
            phone_number=form_data.get('phone_number')
        )
        data_to_save = asset_obj.to_dict()

        if asset_id:
            update_document('assets', asset_id, data_to_save)
            flash('Ativo atualizado com sucesso!', 'success')
        else:
            add_document('assets', data_to_save)
            flash('Ativo adicionado com sucesso!', 'success')
            
    except Exception as e:
        current_app.logger.error(f"Erro ao salvar ativo: {e}", exc_info=True)
        flash('Ocorreu um erro inesperado ao salvar o ativo.', 'danger')
    
    return redirect(url_for('assets.list_assets'))

# ... (Manter as funções de delete, export e import como estão)