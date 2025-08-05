# app/routes/asset_routes.py (Versão Final com Busca e Novas Colunas)

import csv
import datetime
import io
import json
from typing import Any, Dict, List, Optional, Union

import pandas as pd
from firebase_admin import firestore
from flask import (Blueprint, Response, current_app, flash, redirect,
                   render_template, request, url_for)
from werkzeug.wrappers import Response as WerkzeugResponse

from app.auth.routes import login_required, role_required
from app.config import ALLOWED_EXTENSIONS, ASSET_BRANDS, ASSET_STATUS
from app.models.asset import Asset
from app.services.firestore_service import (add_document, delete_document,
                                            get_all_documents, get_document,
                                            get_documents_by_query,
                                            get_documents_with_query,
                                            update_document)
from app.services.storage_service import (delete_file_from_storage,
                                          upload_file_to_storage)

asset_bp = Blueprint('assets', __name__, url_prefix='/assets')


@asset_bp.route('/')
@login_required
def list_assets() -> str:
    """
    Exibe a lista de ativos com funcionalidades de filtro, busca e ordenação.
    """
    try:
        # 1. Obter todos os parâmetros da URL
        sort_by = request.args.get('sort_by', 'brand')
        filter_type = request.args.get('filter_type', '')
        filter_status = request.args.get('filter_status', '')
        search_term = request.args.get('q', '').strip()

        # 2. Construir a lista de filtros para a query
        query_filters = []
        if filter_type:
            query_filters.append({'field': 'assetTypeId', 'op': '==', 'value': filter_type})
        if filter_status:
            query_filters.append({'field': 'status', 'op': '==', 'value': filter_status})
        
        # NOVA LÓGICA DE BUSCA: Busca por prefixo no campo 'model'
        if search_term:
            # Esta combinação de queries simula um "começa com" (case-sensitive)
            query_filters.append({'field': 'model', 'op': '>=', 'value': search_term})
            query_filters.append({'field': 'model', 'op': '<=', 'value': search_term + u'\uf8ff'})

        # 3. Buscar os dados no Firestore
        assets = get_documents_with_query(
            'assets',
            query_params=query_filters,
            order_by=sort_by
        )

        # 4. Enriquecer os dados para exibição, agora incluindo Centros de Custo
        maps = {
            'sectors': {s['id']: s.get('name', 'N/A') for s in get_all_documents('sectors')},
            'assetTypes': {at['id']: at.get('name', 'N/A') for at in get_all_documents('assetTypes')},
            'costCenters': {cc['id']: cc.get('name', 'N/A') for cc in get_all_documents('costCenters')}
        }
        for asset in assets:
            asset['sectorName'] = maps['sectors'].get(asset.get('assignedSectorId'))
            asset['assetTypeName'] = maps['assetTypes'].get(asset.get('assetTypeId'))
            asset['costCenterName'] = maps['costCenters'].get(asset.get('assignedCostCenterId'))
        
        # 5. Preparar o contexto completo para o template
        context = {
            'assets': assets,
            'all_asset_types': get_all_documents('assetTypes'),
            'asset_status_list': ASSET_STATUS,
            'current_filters': {
                'type': filter_type,
                'status': filter_status,
                'q': search_term
            },
            'current_sort': sort_by
        }
        return render_template('assets/list.html', **context)
    
    except Exception as e:
        if 'requires an index' in str(e):
            flash("A combinação de filtro e busca que você tentou requer um índice no Firestore. O link para criação está no log do terminal.", "warning")
        else:
            flash("Ocorreu um erro ao carregar a lista de ativos.", "danger")
        current_app.logger.error(f"Erro ao listar ativos: {e}", exc_info=True)
        return render_template('assets/list.html', assets=[], all_asset_types=get_all_documents('assetTypes'), asset_status_list=ASSET_STATUS, current_filters={}, current_sort='brand')

# --- O RESTANTE DO FICHEIRO PERMANECE IGUAL ---
def _parse_date(date_string: Optional[str], date_format: str = '%d/%m/%Y') -> Optional[datetime.datetime]:
    if not date_string or pd.isna(date_string): return None
    for fmt in (date_format, '%Y-%m-%d'):
        try:
            return datetime.datetime.strptime(str(date_string).strip(), fmt)
        except (ValueError, TypeError):
            continue
    current_app.logger.warning(f"Formato de data não reconhecido para: {date_string}")
    return None

def _get_form_context(asset_data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    asset_data = asset_data or {}
    try:
        return {
            'asset': asset_data,
            'sectors': get_all_documents('sectors'),
            'units': get_all_documents('units'),
            'cost_centers': get_all_documents('costCenters'),
            'suppliers': get_all_documents('suppliers'),
            'asset_types': get_all_documents('assetTypes'),
            'asset_status': ASSET_STATUS,
            'asset_brands': ASSET_BRANDS
        }
    except Exception as e:
        current_app.logger.error(f"Erro ao construir contexto para ativos: {e}", exc_info=True)
        flash("Falha ao carregar dados de apoio (setores, unidades, etc.).", "danger")
        return {'asset': asset_data, 'sectors': [], 'units': [], 'cost_centers': [], 'suppliers': [], 'asset_types': []}

def allowed_file(filename: str) -> bool:
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

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
        flash("Ocorreu um erro ao carregar o formulário.", "danger")
        return redirect(url_for('assets.list_assets'))

@asset_bp.route('/save/', methods=['POST'])
@asset_bp.route('/save/<string:asset_id>', methods=['POST'])
@login_required
@role_required('admin')
def save_asset(asset_id: Optional[str] = None) -> WerkzeugResponse:
    try:
        form_data = request.form
        required_fields = ['asset_type_id', 'brand', 'model', 'status', 'lease_value', 'lease_date', 
                           'assigned_sector_id', 'assigned_unit_id', 'assigned_cost_center_id']
        if not all(form_data.get(f) for f in required_fields):
            flash('Todos os campos obrigatórios (*) devem ser preenchidos.', 'danger')
            return redirect(request.referrer or url_for('assets.asset_form', asset_id=asset_id))

        uploaded_files_info = [
            upload_file_to_storage(file, "assets") 
            for file in request.files.getlist("attachment_files") 
            if file and file.filename
        ]
        
        asset_obj = Asset(
            asset_type_id=form_data.get('asset_type_id'), brand=form_data.get('brand'), model=form_data.get('model'),
            status=form_data.get('status'), lease_value=float(form_data.get('lease_value', 0.0)),
            lease_date=_parse_date(form_data.get('lease_date'), '%Y-%m-%d'),
            assigned_sector_id=form_data.get('assigned_sector_id'),
            assigned_unit_id=form_data.get('assigned_unit_id'),
            assigned_cost_center_id=form_data.get('assigned_cost_center_id'),
            serial_number=form_data.get('serial_number'),
            internal_tag=form_data.get('internal_tag'),
            user=form_data.get('user'),
            responsible=form_data.get('responsible'),
            description=form_data.get('description'),
            supplier_id=form_data.get('supplier_id'),
            invoice_number=form_data.get('invoice_number'),
            contract_duration_months=int(form_data.get('contract_duration_months')) if form_data.get('contract_duration_months') else None,
            receipt_date=_parse_date(form_data.get('receipt_date'), '%Y-%m-%d'),
            invoice_date=_parse_date(form_data.get('invoice_date'), '%Y-%m-%d'),
            delivery_activation_date=_parse_date(form_data.get('delivery_activation_date'), '%Y-%m-%d'),
            contract_end_date=_parse_date(form_data.get('contract_end_date'), '%Y-%m-%d'),
            deactivation_date=_parse_date(form_data.get('deactivation_date'), '%Y-%m-%d'),
            exclusion_date=_parse_date(form_data.get('exclusion_date'), '%Y-%m-%d'),
            operating_system=form_data.get('operating_system'),
            processor=form_data.get('processor'),
            memory=form_data.get('memory'),
            office_version=form_data.get('office_version'),
            imei=form_data.get('imei'),
            phone_number=form_data.get('phone_number'),
            shared_with=json.loads(form_data.get('shared_with_json', '[]')),
            attachments=json.loads(form_data.get('existing_attachments_json', '[]')) + uploaded_files_info
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


@asset_bp.route('/delete/<string:asset_id>', methods=['POST'])
@login_required
@role_required('admin')
def delete_asset(asset_id: str) -> WerkzeugResponse:
    try:
        asset = get_document('assets', asset_id)
        if asset:
            for att in asset.get('attachments', []):
                if att.get('filePath'):
                    delete_file_from_storage(att['filePath'])
            delete_document('assets', asset_id)
            flash(f'Ativo "{asset.get("model", asset_id)}" e seus anexos foram excluídos com sucesso!', 'success')
        else:
            flash('Ativo não encontrado.', 'danger')
    except Exception as e:
        current_app.logger.error(f"Erro ao excluir ativo {asset_id}: {e}", exc_info=True)
        flash('Erro ao excluir o ativo.', 'danger')
    return redirect(url_for('assets.list_assets'))


@asset_bp.route('/export/csv')
@login_required
def export_assets_csv() -> Union[Response, WerkzeugResponse]:
    try:
        all_assets = get_all_documents('assets')
        if not all_assets:
            flash("Não há ativos para exportar.", "info")
            return redirect(url_for('assets.list_assets'))
        
        maps = {
            'assetTypes': {at['id']: at.get('name', '') for at in get_all_documents('assetTypes')},
            'sectors': {s['id']: s.get('name', '') for s in get_all_documents('sectors')},
            'units': {u['id']: u.get('name', '') for u in get_all_documents('units')},
            'suppliers': {s['id']: s.get('name', '') for s in get_all_documents('suppliers')},
            'costCenters': {c['id']: c.get('name', '') for c in get_all_documents('costCenters')}
        }
        
        output = io.StringIO()
        writer = csv.writer(output, delimiter=';', lineterminator='\n')
        
        headers = ['ID', 'Tipo de Ativo', 'Marca', 'Modelo', 'Num Serie', 'Tag Interno', 'Status', 'Utilizador', 'Responsavel', 'Valor', 'Data Contrato', 'Setor', 'Unidade', 'Centro de Custo', 'Fornecedor', 'SO', 'Processador', 'Memoria', 'Office', 'Data Recebimento', 'Data Entrega/Ativacao']
        writer.writerow(headers)

        for asset in all_assets:
            row = [
                asset.get('id', ''), maps['assetTypes'].get(asset.get('assetTypeId'), ''), asset.get('brand', ''),
                asset.get('model', ''), asset.get('serialNumber', ''), asset.get('internalTag', ''), asset.get('status', ''),
                asset.get('user', ''), asset.get('responsible', ''),
                str(asset.get('leaseValue', '')).replace('.', ','),
                asset.get('leaseDate').strftime('%d/%m/%Y') if isinstance(asset.get('leaseDate'), datetime.datetime) else '',
                maps['sectors'].get(asset.get('assignedSectorId'), ''),
                maps['units'].get(asset.get('assignedUnitId'), ''),
                maps['costCenters'].get(asset.get('assignedCostCenterId'), ''),
                maps['suppliers'].get(asset.get('supplierId'), ''),
                asset.get('operatingSystem'), asset.get('processor'), asset.get('memory'), asset.get('officeVersion'),
                asset.get('receiptDate').strftime('%d/%m/%Y') if isinstance(asset.get('receiptDate'), datetime.datetime) else '',
                asset.get('deliveryActivationDate').strftime('%d/%m/%Y') if isinstance(asset.get('deliveryActivationDate'), datetime.datetime) else ''
            ]
            writer.writerow([field if field is not None else '' for field in row])
        
        output.seek(0)
        return Response(output.getvalue(), mimetype="text/csv", headers={"Content-Disposition": "attachment;filename=export_ativos.csv"})
    except Exception as e:
        current_app.logger.error(f"Erro ao exportar ativos: {e}", exc_info=True)
        flash("Ocorreu um erro ao gerar o ficheiro de exportação.", "danger")
        return redirect(url_for('assets.list_assets'))


@asset_bp.route('/import', methods=['GET', 'POST'])
@login_required
@role_required('admin')
def import_assets_csv() -> Union[str, WerkzeugResponse]:
    if request.method == 'POST':
        if 'csv_file' not in request.files or not request.files['csv_file'].filename:
            flash('Nenhum ficheiro selecionado.', 'danger')
            return redirect(request.url)
        
        file = request.files['csv_file']
        if not file or not allowed_file(file.filename):
            flash('Tipo de ficheiro não permitido. Apenas .csv é aceite.', 'danger')
            return redirect(request.url)

        try:
            maps = {
                'assetTypes': {at.get('name', '').lower(): at['id'] for at in get_all_documents('assetTypes')},
                'sectors': {s.get('name', '').lower(): s['id'] for s in get_all_documents('sectors')},
                'units': {u.get('name', '').lower(): u['id'] for u in get_all_documents('units')},
                'suppliers': {s.get('name', '').lower(): s['id'] for s in get_all_documents('suppliers')},
                'costCenters': {c.get('name', '').lower(): c['id'] for c in get_all_documents('costCenters')}
            }
            df = pd.read_csv(io.StringIO(file.stream.read().decode('latin1')), delimiter=';', keep_default_na=False)
            imported_count, updated_count, errors = 0, 0, []

            for index, row in df.iterrows():
                try:
                    serial_number = str(row.get('Num Serie', '')).strip()
                    if not serial_number:
                        errors.append(f"Linha {index + 2}: 'Num Serie' é obrigatório para importação.")
                        continue

                    asset_type_id = maps['assetTypes'].get(str(row.get('Tipo de Ativo', '')).lower())
                    sector_id = maps['sectors'].get(str(row.get('Setor', '')).lower())
                    unit_id = maps['units'].get(str(row.get('Unidade', '')).lower())
                    supplier_id = maps['suppliers'].get(str(row.get('Fornecedor', '')).lower()) if row.get('Fornecedor') else None
                    cost_center_id = maps['costCenters'].get(str(row.get('Centro de Custo', '')).lower())

                    if not all([asset_type_id, sector_id, unit_id, cost_center_id]):
                        errors.append(f"Linha {index + 2}: Tipo de Ativo, Setor, Unidade ou Centro de Custo não encontrado(s).")
                        continue

                    asset_obj = Asset(
                        asset_type_id=asset_type_id, brand=row.get('Marca'), model=row.get('Modelo'),
                        status=row.get('Status'), serial_number=serial_number,
                        lease_value=float(str(row.get('Valor Locacao', 0.0)).replace(',', '.')),
                        lease_date=_parse_date(row.get('Data Locacao')),
                        assigned_sector_id=sector_id, assigned_unit_id=unit_id,
                        assigned_cost_center_id=cost_center_id,
                        supplier_id=supplier_id, user=row.get('Utilizador'),
                        responsible=row.get('Responsavel'), operating_system=row.get('SO'),
                        processor=row.get('Processador'), memory=row.get('Memoria'),
                        office_version=row.get('Office'), internal_tag=row.get('Tag Interno'),
                        receipt_date=_parse_date(row.get('Data Recebimento')),
                    )
                    
                    data = asset_obj.to_dict()
                    existing_assets = get_documents_by_query('assets', 'serialNumber', '==', serial_number)
                    if existing_assets:
                        update_document('assets', existing_assets[0]['id'], data)
                        updated_count += 1
                    else:
                        add_document('assets', data)
                        imported_count += 1
                except Exception as e:
                    errors.append(f"Linha {index + 2} (SN: {serial_number}): {e}")

            if imported_count: flash(f'{imported_count} ativos importados.', 'success')
            if updated_count: flash(f'{updated_count} ativos atualizados.', 'info')
            if errors: flash(f'{len(errors)} linhas com erros.', 'danger')

        except Exception as e:
            current_app.logger.error(f"Erro na importação: {e}", exc_info=True)
            flash('Ocorreu um erro geral ao processar o ficheiro.', 'danger')
        return redirect(url_for('assets.list_assets'))
    return render_template('assets/import_form.html')


@asset_bp.route('/export/template/csv')
@login_required
def download_asset_template_csv() -> Response:
    """Fornece o template CSV para download."""
    output = io.StringIO()
    writer = csv.writer(output, delimiter=';', lineterminator='\n')
    headers = ['Tipo de Ativo', 'Marca', 'Modelo', 'Status', 'Valor Locacao', 'Data Locacao', 'Setor', 'Unidade', 'Centro de Custo', 'Fornecedor', 'Num Serie', 'Utilizador', 'Responsavel', 'SO', 'Processador', 'Memoria', 'Office', 'Tag Interno', 'Data Recebimento']
    writer.writerow(headers)
    writer.writerow(['Notebook', 'Dell', 'Latitude 5420', 'Ativo', '150.50', '15/01/2023', 'Tecnologia da Informação', 'Matriz', 'TI-Infra', 'Fornecedor A', 'ABC-123', 'Utilizador Exemplo', 'Responsável TI', 'Windows 11 Pro', 'Intel i5', '16GB DDR4', 'Office 365', 'TAG-001', '14/01/2023'])
    output.seek(0)
    return Response(output.getvalue(), mimetype="text/csv", headers={"Content-Disposition": "attachment;filename=template_import_ativos.csv"})