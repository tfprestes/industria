# app/routes/contract_routes.py

import datetime
from typing import Any, Dict, List, Optional, Union

from flask import (Blueprint, Response, current_app, flash, redirect,
                   render_template, request, url_for)
from werkzeug.wrappers import Response as WerkzeugResponse
from firebase_admin import firestore

from app.auth.routes import login_required, role_required
from app.models.contract import Contract
from app.services.firestore_service import (add_document, delete_document,
                                            get_all_documents, get_document,
                                            get_documents_with_query,
                                            update_document)

contract_bp = Blueprint(
    'contracts', 
    __name__, 
    url_prefix='/contracts'
)

def _get_context_data() -> Dict[str, Any]:
    """Busca dados de apoio para os formulários (setores, fornecedores, etc.)."""
    try:
        return {
            'sectors': get_all_documents('sectors'),
            'suppliers': get_all_documents('suppliers'),
            'billing_cycles': ['Mensal', 'Trimestral', 'Semestral', 'Anual', 'Único'],
            'status_options': ['Ativo', 'Pendente', 'Expirado', 'Cancelado']
        }
    except Exception as e:
        current_app.logger.error(f"Erro ao buscar dados de contexto para contratos: {e}", exc_info=True)
        return {'sectors': [], 'suppliers': [], 'billing_cycles': [], 'status_options': []}

def _parse_date_from_form(date_string: Optional[str]) -> Optional[datetime.datetime]:
    """Converte uma string 'AAAA-MM-DD' de um formulário para um objeto datetime."""
    if not date_string:
        return None
    try:
        return datetime.datetime.strptime(date_string, '%Y-%m-%d')
    except (ValueError, TypeError):
        return None

@contract_bp.route('/')
@login_required
def list_contracts() -> str:
    """Exibe a lista de todos os contratos."""
    try:
        contracts = get_all_documents('contracts')
        suppliers_map = {s['id']: s.get('name', 'N/A') for s in get_all_documents('suppliers')}
        sectors_map = {s['id']: s.get('name', 'N/A') for s in get_all_documents('sectors')}
        for contract in contracts:
            contract['supplierName'] = suppliers_map.get(contract.get('supplierId'), 'N/A')
            contract['sectorName'] = sectors_map.get(contract.get('assignedSectorId'), 'N/A')
        return render_template('contracts/list.html', contracts=contracts)
    except Exception as e:
        current_app.logger.error(f"Erro ao listar contratos: {e}", exc_info=True)
        flash("Ocorreu um erro ao carregar a lista de contratos.", "danger")
        return render_template('contracts/list.html', contracts=[])

@contract_bp.route('/form', methods=['GET'])
@contract_bp.route('/form/<string:contract_id>', methods=['GET'])
@login_required
@role_required('admin')
def contract_form(contract_id: Optional[str] = None) -> Union[str, WerkzeugResponse]:
    """Exibe o formulário para adicionar ou editar um contrato."""
    try:
        contract_data = {}
        if contract_id:
            contract_data = get_document('contracts', contract_id)
            if not contract_data:
                flash('Contrato não encontrado.', 'danger')
                return redirect(url_for('contracts.list_contracts'))
        
        context = _get_context_data()
        context['contract'] = contract_data
        
        return render_template('contracts/form.html', **context)
    except Exception as e:
        current_app.logger.error(f"Erro ao carregar formulário de contrato: {e}", exc_info=True)
        flash("Ocorreu um erro ao carregar o formulário.", "danger")
        return redirect(url_for('contracts.list_contracts'))


# --- CORREÇÃO APLICADA AQUI ---
# Adicionada a barra '/' no final da rota '/save/' para corresponder ao que o formulário envia.
@contract_bp.route('/save/', methods=['POST'])
@contract_bp.route('/save/<string:contract_id>', methods=['POST'])
@login_required
@role_required('admin')
def save_contract(contract_id: Optional[str] = None) -> WerkzeugResponse:
    """Salva um novo contrato ou atualiza um existente."""
    try:
        form = request.form
        contract_obj = Contract(
            id=contract_id,
            name=form.get('name'),
            supplierId=form.get('supplierId'),
            category=form.get('category'),
            value=float(form.get('value', 0.0)),
            billingCycle=form.get('billingCycle'),
            paymentDay=int(form.get('paymentDay', 1)),
            startDate=_parse_date_from_form(form.get('startDate')),
            endDate=_parse_date_from_form(form.get('endDate')),
            status=form.get('status'),
            assignedSectorId=form.get('assignedSectorId'),
            notes=form.get('notes')
        )
        data_to_save = contract_obj.to_dict()

        if contract_id:
            update_document('contracts', contract_id, data_to_save)
            flash(f'Contrato "{contract_obj.name}" atualizado com sucesso!', 'success')
        else:
            add_document('contracts', data_to_save)
            flash(f'Contrato "{contract_obj.name}" criado com sucesso!', 'success')

        return redirect(url_for('contracts.list_contracts'))
    except Exception as e:
        current_app.logger.error(f"Erro ao salvar contrato: {e}", exc_info=True)
        flash("Ocorreu um erro inesperado ao salvar o contrato.", "danger")
        return redirect(url_for('contracts.list_contracts'))

@contract_bp.route('/delete/<string:contract_id>', methods=['POST'])
@login_required
@role_required('admin')
def delete_contract(contract_id: str) -> WerkzeugResponse:
    """Exclui um contrato."""
    try:
        contract = get_document('contracts', contract_id)
        if contract:
            delete_document('contracts', contract_id)
            flash(f'Contrato "{contract.get("name", "N/A")}" excluído com sucesso!', 'success')
        else:
            flash('Contrato não encontrado.', 'danger')
    except Exception as e:
        current_app.logger.error(f"Erro ao excluir contrato {contract_id}: {e}", exc_info=True)
        flash('Ocorreu um erro ao excluir o contrato.', 'danger')
        
    return redirect(url_for('contracts.list_contracts'))