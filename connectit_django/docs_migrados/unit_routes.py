# app/routes/unit_routes.py

"""
Módulo de rotas para a gestão de Unidades (Cadastros Mestres).

Este blueprint define os endpoints para todas as operações CRUD (Criar, Ler, 
Atualizar, Excluir) para a entidade 'Unidades', que representa as localizações
físicas da empresa (matriz e filiais).
"""

from typing import Any, Dict, List, Optional

from firebase_admin import firestore
from flask import (Blueprint, Response, current_app, flash, redirect,
                   render_template, request, url_for)
from werkzeug.wrappers import Response as WerkzeugResponse

from app.auth.routes import login_required, role_required
from app.services.firestore_service import (add_document, delete_document,
                                            get_all_documents, get_document,
                                            update_document)

unit_bp = Blueprint(
    'units',
    __name__,
    url_prefix='/units'
)


@unit_bp.route('/')
@login_required
@role_required('admin', 'viewer')
def list_units() -> str:
    """
    Exibe a lista de todas as Unidades (matriz e filiais).

    Returns:
        str: O template da lista de unidades renderizado.
    """
    try:
        units: List[Dict[str, Any]] = get_all_documents('units')
        return render_template('settings/units_list.html', units=units)
    except Exception as e:
        current_app.logger.error(f"Erro ao listar unidades: {e}", exc_info=True)
        flash("Ocorreu um erro crítico ao carregar os dados das unidades.", "danger")
        return render_template('settings/units_list.html', units=[])


@unit_bp.route('/form', methods=['GET'])
@unit_bp.route('/form/<string:unit_id>', methods=['GET'])
@login_required
@role_required('admin')
def unit_form(unit_id: Optional[str] = None) -> str | WerkzeugResponse:
    """
    Exibe um formulário unificado para adicionar ou editar uma Unidade.

    Args:
        unit_id (Optional[str]): O ID da unidade a ser editada.
                                 Se None, exibe um formulário em branco para criação.

    Returns:
        Union[str, WerkzeugResponse]: O template do formulário renderizado ou um
                                      redirecionamento se a unidade não for encontrada.
    """
    try:
        unit: Dict[str, Any] = get_document('units', unit_id) if unit_id else {}
        if unit_id and not unit:
            flash('Unidade não encontrada.', 'danger')
            return redirect(url_for('units.list_units'))
        
        return render_template('settings/unit_form.html', unit=unit)
    except Exception as e:
        current_app.logger.error(f"Erro ao carregar formulário de unidade: {e}", exc_info=True)
        flash("Ocorreu um erro ao carregar o formulário.", "danger")
        return redirect(url_for('units.list_units'))


@unit_bp.route('/save/', methods=['POST'])
@unit_bp.route('/save/<string:unit_id>', methods=['POST'])
@login_required
@role_required('admin')
def save_unit(unit_id: Optional[str] = None) -> WerkzeugResponse:
    """
    Processa a submissão do formulário para criar ou atualizar uma Unidade.

    Args:
        unit_id (Optional[str]): O ID da unidade a ser atualizada.
                                 Se None, cria uma nova.

    Returns:
        WerkzeugResponse: Um redirecionamento para a lista de unidades.
    """
    try:
        form_data: Dict[str, Any] = request.form
        
        required_fields = ['name', 'type', 'address_street', 'address_city', 'address_state', 'address_zip_code', 'address_country']
        if not all(form_data.get(f) for f in required_fields):
            flash('Nome, Tipo e os campos principais do Endereço são obrigatórios.', 'danger')
            return render_template('settings/unit_form.html', unit=dict(form_data))
        
        # Constrói o sub-documento de endereço, omitindo campos vazios
        address_data = {
            key: form_data.get(f"address_{key}")
            for key in ['street', 'number', 'complement', 'neighborhood', 'city', 'state', 'zipCode', 'country']
            if form_data.get(f"address_{key}")
        }
        
        data_to_save: Dict[str, Any] = {
            'name': form_data.get('name'),
            'type': form_data.get('type'),
            'address': address_data
        }
        
        # Lógica para campos opcionais, usando DELETE_FIELD apenas em atualizações
        for field in ['cnpj', 'description']:
            value = form_data.get(field)
            if value:
                data_to_save[field] = value
            elif unit_id:
                data_to_save[field] = firestore.DELETE_FIELD

        if unit_id:
            update_document('units', unit_id, data_to_save)
            flash(f'Unidade "{data_to_save["name"]}" atualizada com sucesso!', 'success')
        else:
            add_document('units', data_to_save)
            flash(f'Unidade "{data_to_save["name"]}" criada com sucesso!', 'success')
            
    except Exception as e:
        current_app.logger.error(f"Erro ao salvar unidade: {e}", exc_info=True)
        flash("Ocorreu um erro inesperado ao salvar a unidade.", "danger")

    return redirect(url_for('units.list_units'))


@unit_bp.route('/delete/<string:unit_id>', methods=['POST'])
@login_required
@role_required('admin')
def delete_unit(unit_id: str) -> WerkzeugResponse:
    """
    Exclui uma Unidade, após verificar se não há dependências.

    Args:
        unit_id (str): O ID da unidade a ser excluída.

    Returns:
        WerkzeugResponse: Um redirecionamento para a lista de unidades.
    """
    try:
        # TODO: Implementar verificação de dependência (se ativos, etc., usam esta unidade)
        unit = get_document('units', unit_id)
        if not unit:
            flash('Unidade não encontrada.', 'danger')
        else:
            delete_document('units', unit_id)
            flash(f'Unidade "{unit.get("name")}" excluída com sucesso!', 'success')
    except Exception as e:
        current_app.logger.error(f"Erro ao excluir unidade {unit_id}: {e}", exc_info=True)
        flash('Erro ao excluir a unidade.', 'danger')
        
    return redirect(url_for('units.list_units'))