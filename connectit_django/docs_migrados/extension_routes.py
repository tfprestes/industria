# app/routes/extension_routes.py

"""
Módulo de rotas para a gestão de Ramais Telefónicos.

Este blueprint define os endpoints para as operações CRUD da entidade 'extensions',
permitindo manter uma lista de consulta de ramais associados a colaboradores,
setores e unidades.
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

extension_bp = Blueprint(
    'extensions',
    __name__,
    url_prefix='/extensions'
)


def _get_form_context(extension_data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """
    Constrói e retorna o dicionário de contexto para os templates de ramais.

    Args:
        extension_data (Optional[Dict[str, Any]]): Dados de um ramal para pré-preencher
                                                    o formulário. Defaults to None.
    Returns:
        Dict[str, Any]: O contexto para renderização do template.
    """
    if extension_data is None:
        extension_data = {}
    try:
        context = {
            'extension': extension_data,
            'sectors': get_all_documents('sectors'),
            'units': get_all_documents('units')
        }
        return context
    except Exception as e:
        current_app.logger.error(f"Erro ao construir contexto para ramais: {e}", exc_info=True)
        flash("Falha ao carregar dados de apoio (Setores/Unidades).", "danger")
        return {'extension': extension_data, 'sectors': [], 'units': []}


@extension_bp.route('/')
@login_required
@role_required('admin', 'viewer')
def list_extensions() -> str:
    """Exibe a lista de todos os ramais telefónicos."""
    try:
        extensions: List[Dict[str, Any]] = get_all_documents('extensions')
        sectors_map: Dict[str, str] = {s['id']: s.get('name', 'N/A') for s in get_all_documents('sectors')}
        units_map: Dict[str, str] = {u['id']: u.get('name', 'N/A') for u in get_all_documents('units')}
        
        for ext in extensions:
            ext['sectorName'] = sectors_map.get(ext.get('sectorId'), 'N/A')
            ext['unitName'] = units_map.get(ext.get('unitId'), 'N/A')

        return render_template('extensions/list.html', extensions=extensions)
    except Exception as e:
        current_app.logger.error(f"Erro ao listar ramais: {e}", exc_info=True)
        flash("Ocorreu um erro ao carregar a lista de ramais.", "danger")
        return render_template('extensions/list.html', extensions=[])


@extension_bp.route('/form', methods=['GET'])
@extension_bp.route('/form/<string:extension_id>', methods=['GET'])
@login_required
@role_required('admin')
def extension_form(extension_id: Optional[str] = None) -> str | WerkzeugResponse:
    """Exibe o formulário para adicionar ou editar um ramal."""
    try:
        extension: Dict[str, Any] = get_document('extensions', extension_id) if extension_id else {}
        if extension_id and not extension:
            flash('Ramal não encontrado.', 'danger')
            return redirect(url_for('extensions.list_extensions'))
        
        context = _get_form_context(extension)
        return render_template('extensions/form.html', **context)
    except Exception as e:
        current_app.logger.error(f"Erro ao carregar formulário de ramal: {e}", exc_info=True)
        flash("Ocorreu um erro ao carregar o formulário.", "danger")
        return redirect(url_for('extensions.list_extensions'))


@extension_bp.route('/save/', methods=['POST'])
@extension_bp.route('/save/<string:extension_id>', methods=['POST'])
@login_required
@role_required('admin')
def save_extension(extension_id: Optional[str] = None) -> WerkzeugResponse:
    """Salva um novo ramal ou atualiza um existente."""
    try:
        form_data: Dict[str, Any] = request.form
        
        # Correção: Nomes dos campos em snake_case para corresponder ao HTML
        required_fields = ['number', 'user_name', 'sector_id', 'unit_id']
        if not all(form_data.get(f) for f in required_fields):
            flash('Todos os campos obrigatórios (*) devem ser preenchidos.', 'danger')
            context = _get_form_context(dict(form_data))
            return render_template('extensions/form.html', **context)

        data_to_save: Dict[str, Any] = {
            'number': form_data.get('number'),
            'userName': form_data.get('user_name'),
            'sectorId': form_data.get('sector_id'),
            'unitId': form_data.get('unit_id'),
        }

        # Lógica corrigida para o campo opcional 'notes'
        notes = form_data.get('notes')
        if notes:
            data_to_save['notes'] = notes
        elif extension_id:
            data_to_save['notes'] = firestore.DELETE_FIELD

        if extension_id:
            update_document('extensions', extension_id, data_to_save)
            flash('Ramal atualizado com sucesso!', 'success')
        else:
            add_document('extensions', data_to_save)
            flash('Ramal registado com sucesso!', 'success')

    except Exception as e:
        current_app.logger.error(f"Erro ao salvar ramal: {e}", exc_info=True)
        flash(f'Ocorreu um erro inesperado ao salvar o ramal: {e}', 'danger')
    
    return redirect(url_for('extensions.list_extensions'))


@extension_bp.route('/delete/<string:extension_id>', methods=['POST'])
@login_required
@role_required('admin')
def delete_extension(extension_id: str) -> WerkzeugResponse:
    """Exclui um ramal."""
    try:
        extension = get_document('extensions', extension_id)
        if extension:
            delete_document('extensions', extension_id)
            flash(f'Ramal "{extension.get("number", extension_id)}" excluído com sucesso!', 'success')
        else:
            flash('Ramal não encontrado.', 'danger')
    except Exception as e:
        current_app.logger.error(f"Erro ao excluir ramal {extension_id}: {e}", exc_info=True)
        flash(f'Erro ao excluir ramal: {e}', 'danger')
        
    return redirect(url_for('extensions.list_extensions'))