# app/routes/inventory_routes.py

"""
Módulo de rotas para a gestão de Estoque.

Define os endpoints para as operações CRUD da entidade 'inventory', que
controla os componentes, consumíveis e outras peças da empresa.
Inclui lógicas para verificação de stock baixo e dependências em
registos de manutenção.
"""

from typing import Any, Dict, List, Optional, Union

from firebase_admin import firestore
from flask import (Blueprint, Response, current_app, flash, redirect,
                   render_template, request, url_for)
from werkzeug.wrappers import Response as WerkzeugResponse

from app.auth.routes import login_required, role_required
from app.config import INVENTORY_ITEM_TYPES, INVENTORY_UNITS_OF_MEASURE
from app.services.firestore_service import (add_document, delete_document,
                                            get_all_documents, get_document,
                                            get_documents_by_query,
                                            update_document)


inventory_bp = Blueprint(
    'inventory',
    __name__,
    url_prefix='/inventory'
)


def _build_inventory_context(item_data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """
    Constrói o dicionário de contexto para os templates de estoque.

    Args:
        item_data (Optional[Dict[str, Any]]): Dados de um item para pré-preencher
                                              o formulário. Defaults to None.

    Returns:
        Dict[str, Any]: O contexto para renderização do template.
    """
    if item_data is None:
        item_data = {}
    try:
        suppliers: List[Dict[str, Any]] = get_all_documents('suppliers')
    except Exception as e:
        current_app.logger.error(f"Erro ao buscar fornecedores para o contexto: {e}")
        flash("Falha ao carregar a lista de fornecedores.", "warning")
        suppliers = []
        
    return {
        'item': item_data,
        'item_types': INVENTORY_ITEM_TYPES,
        'units_of_measure': INVENTORY_UNITS_OF_MEASURE,
        'suppliers': suppliers
    }


@inventory_bp.route('/')
@login_required
@role_required('admin', 'viewer')
def list_inventory_items() -> str:
    """Exibe a lista de todos os itens de estoque."""
    try:
        inventory_items: List[Dict[str, Any]] = get_all_documents('inventory')
        for item in inventory_items:
            quantity = item.get('quantity', 0)
            min_level = item.get('minStockLevel', 0)
            item['low_stock'] = min_level > 0 and quantity <= min_level
        return render_template('inventory/list.html', inventory_items=inventory_items)
    except Exception as e:
        current_app.logger.error(f"Erro ao listar itens de estoque: {e}", exc_info=True)
        flash("Ocorreu um erro ao carregar o estoque.", "danger")
        return render_template('inventory/list.html', inventory_items=[])


@inventory_bp.route('/form', methods=['GET'])
@inventory_bp.route('/form/<string:item_id>', methods=['GET'])
@login_required
@role_required('admin')
def inventory_item_form(item_id: Optional[str] = None) -> Union[str, WerkzeugResponse]:
    """Exibe o formulário para adicionar ou editar um item de estoque."""
    try:
        item: Dict[str, Any] = get_document('inventory', item_id) if item_id else {}
        if item_id and not item:
            flash('Item de estoque não encontrado.', 'danger')
            return redirect(url_for('inventory.list_inventory_items'))
        
        context = _build_inventory_context(item)
        return render_template('inventory/form.html', **context)
    except Exception as e:
        current_app.logger.error(f"Erro ao carregar formulário de estoque: {e}", exc_info=True)
        flash("Ocorreu um erro ao carregar o formulário.", "danger")
        return redirect(url_for('inventory.list_inventory_items'))


@inventory_bp.route('/save/', methods=['POST'])
@inventory_bp.route('/save/<string:item_id>', methods=['POST'])
@login_required
@role_required('admin')
def save_inventory_item(item_id: Optional[str] = None) -> WerkzeugResponse:
    """Salva um novo item de estoque ou atualiza um existente."""
    try:
        form_data: Dict[str, Any] = request.form
        
        required_fields = ['item_name', 'item_type', 'quantity', 'unit_of_measure']
        if not all(form_data.get(f) for f in required_fields):
            flash('Todos os campos obrigatórios (*) devem ser preenchidos.', 'danger')
            context = _build_inventory_context(dict(form_data))
            return render_template('inventory/form.html', **context)

        data_to_save: Dict[str, Any] = {
            'itemName': form_data.get('item_name'),
            'itemType': form_data.get('item_type'),
            'quantity': int(form_data.get('quantity', 0)),
            'unitOfMeasure': form_data.get('unit_of_measure'),
        }

        optional_fields = ['min_stock_level', 'supplier_id', 'location_description']
        firestore_keys = ['minStockLevel', 'supplierId', 'locationDescription']
        
        for form_key, firestore_key in zip(optional_fields, firestore_keys):
            value = form_data.get(form_key)
            if value:
                data_to_save[firestore_key] = int(value) if form_key == 'min_stock_level' else value
            elif item_id:
                data_to_save[firestore_key] = firestore.DELETE_FIELD

        if item_id:
            update_document('inventory', item_id, data_to_save)
            flash(f'Item "{data_to_save["itemName"]}" atualizado com sucesso!', 'success')
        else:
            add_document('inventory', data_to_save)
            flash(f'Item "{data_to_save["itemName"]}" adicionado com sucesso!', 'success')

    except Exception as e:
        current_app.logger.error(f"Erro ao salvar item de estoque: {e}", exc_info=True)
        flash(f'Ocorreu um erro inesperado ao salvar o item: {e}', 'danger')
    
    return redirect(url_for('inventory.list_inventory_items'))


@inventory_bp.route('/delete/<string:item_id>', methods=['POST'])
@login_required
@role_required('admin')
def delete_inventory_item(item_id: str) -> WerkzeugResponse:
    """Exclui um item de estoque, verificando se não está em uso."""
    try:
        query_results = get_documents_by_query('maintenanceLogs', 'partsUsed.itemId', '==', item_id)
        if query_results:
            flash('Este item não pode ser excluído pois está associado a um ou mais registos de manutenção.', 'danger')
            return redirect(url_for('inventory.list_inventory_items'))

        item = get_document('inventory', item_id)
        if item:
            delete_document('inventory', item_id)
            flash(f'Item "{item.get("itemName", item_id)}" excluído com sucesso!', 'success')
        else:
            flash('Item de estoque não encontrado.', 'danger')
            
    except Exception as e:
        current_app.logger.error(f"Erro ao excluir item de estoque {item_id}: {e}", exc_info=True)
        flash(f'Erro ao excluir item: {e}', 'danger')
        
    return redirect(url_for('inventory.list_inventory_items'))