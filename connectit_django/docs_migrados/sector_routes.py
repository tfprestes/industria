# app/routes/sector_routes.py

"""
Módulo de rotas para a gestão de Setores (Cadastros Mestres).

Este blueprint lida com todas as operações CRUD (Criar, Ler, Atualizar, Excluir)
para a coleção 'sectors' no Firestore, utilizando uma arquitetura consistente
com formulário unificado e rotas de salvamento.
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

sector_bp = Blueprint(
    'sectors',
    __name__,
    url_prefix='/sectors'
)


def _get_form_context(form_data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """
    Constrói e retorna o dicionário de contexto para os templates de setor.

    Busca os centros de custo para popular os menus de seleção e utiliza
    os dados do formulário fornecidos para pré-preencher o formulário em
    casos de erro de validação.

    Args:
        form_data (Optional[Dict[str, Any]]): Dados do formulário submetido
            para pré-preenchimento. Defaults to None.

    Returns:
        Dict[str, Any]: O contexto para renderização do template.
    """
    if form_data is None:
        form_data = {}
    try:
        cost_centers: List[Dict[str, Any]] = get_all_documents('costCenters')
    except Exception as e:
        current_app.logger.error(f"Erro ao buscar centros de custo: {e}")
        flash("Falha ao carregar dados de apoio (Centros de Custo).", "danger")
        cost_centers = []
    
    return {
        'sector': form_data,
        'cost_centers': cost_centers
    }


@sector_bp.route('/')
@login_required
@role_required('admin', 'viewer')
def list_sectors() -> str:
    """
    Exibe a lista de todos os setores.

    Busca todos os setores e centros de custo para enriquecer os dados
    da lista com os nomes dos centros de custo associados.

    Returns:
        str: O template da lista de setores renderizado.
    """
    try:
        sectors: List[Dict[str, Any]] = get_all_documents('sectors')
        cost_centers_map: Dict[str, str] = {
            cc['id']: cc.get('name', 'N/A') for cc in get_all_documents('costCenters')
        }
        for sector in sectors:
            sector['costCenterName'] = cost_centers_map.get(
                sector.get('associatedCostCenterId'), 'Não associado'
            )
        return render_template('settings/sectors_list.html', sectors=sectors)
    except Exception as e:
        current_app.logger.error(f"Erro ao listar setores: {e}", exc_info=True)
        flash("Ocorreu um erro crítico ao carregar os dados dos setores.", "danger")
        return render_template('settings/sectors_list.html', sectors=[])


@sector_bp.route('/form', methods=['GET'])
@sector_bp.route('/form/<string:sector_id>', methods=['GET'])
@login_required
@role_required('admin')
def sector_form(sector_id: Optional[str] = None) -> str | WerkzeugResponse:
    """
    Exibe um formulário unificado para adicionar ou editar um setor.

    Args:
        sector_id (Optional[str]): O ID do setor a ser editado.
                                   Se None, exibe um formulário em branco.

    Returns:
        Union[str, WerkzeugResponse]: O template do formulário renderizado ou um
                                      redirecionamento se o setor não for encontrado.
    """
    try:
        sector_data: Dict[str, Any] = get_document('sectors', sector_id) if sector_id else {}
        if sector_id and not sector_data:
            flash('Setor não encontrado.', 'danger')
            return redirect(url_for('sectors.list_sectors'))
        
        context = _get_form_context(sector_data)
        return render_template('settings/sector_form.html', **context)
    except Exception as e:
        current_app.logger.error(f"Erro ao carregar formulário de setor: {e}", exc_info=True)
        flash("Ocorreu um erro ao carregar o formulário.", "danger")
        return redirect(url_for('sectors.list_sectors'))


@sector_bp.route('/save/', methods=['POST'])
@sector_bp.route('/save/<string:sector_id>', methods=['POST'])
@login_required
@role_required('admin')
def save_sector(sector_id: Optional[str] = None) -> WerkzeugResponse:
    """
    Processa a submissão do formulário para criar ou atualizar um setor.

    Args:
        sector_id (Optional[str]): O ID do setor a ser atualizado.
                                   Se None, cria um novo setor.

    Returns:
        WerkzeugResponse: Um redirecionamento para a lista de setores.
    """
    try:
        form_data: Dict[str, Any] = request.form
        
        # Correção: O nome do campo no HTML é 'associated_cost_center_id'
        if not form_data.get('name') or not form_data.get('associated_cost_center_id'):
            flash('Nome do setor e Centro de Custo são campos obrigatórios.', 'danger')
            context = _get_form_context(dict(form_data))
            return render_template('settings/sector_form.html', **context)
            
        data_to_save: Dict[str, Any] = {
            'name': form_data.get('name'),
            'associatedCostCenterId': form_data.get('associated_cost_center_id')
        }

        description = form_data.get('description')
        if description:
            data_to_save['description'] = description
        elif sector_id:
            data_to_save['description'] = firestore.DELETE_FIELD
        
        if sector_id:
            update_document('sectors', sector_id, data_to_save)
            flash(f'Setor "{data_to_save["name"]}" atualizado com sucesso!', 'success')
        else:
            add_document('sectors', data_to_save)
            flash(f'Setor "{data_to_save["name"]}" criado com sucesso!', 'success')
            
    except Exception as e:
        current_app.logger.error(f"Erro ao salvar setor: {e}", exc_info=True)
        flash("Ocorreu um erro inesperado ao salvar o setor.", "danger")

    return redirect(url_for('sectors.list_sectors'))


@sector_bp.route('/delete/<string:sector_id>', methods=['POST'])
@login_required
@role_required('admin')
def delete_sector(sector_id: str) -> WerkzeugResponse:
    """
    Exclui um setor específico, com verificação de segurança.

    Args:
        sector_id (str): O ID do setor a ser excluído.

    Returns:
        WerkzeugResponse: Um redirecionamento para a lista de setores.
    """
    try:
        # TODO: A verificação de dependência pode ser expandida para outros módulos.
        sector = get_document('sectors', sector_id)
        if not sector:
            flash('Setor não encontrado.', 'danger')
        else:
            delete_document('sectors', sector_id)
            flash(f'Setor "{sector.get("name", sector_id)}" excluído com sucesso!', 'success')
    except Exception as e:
        current_app.logger.error(f"Erro ao excluir setor {sector_id}: {e}", exc_info=True)
        flash('Erro ao excluir o setor.', 'danger')
        
    return redirect(url_for('sectors.list_sectors'))