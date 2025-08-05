"""
Módulo de rotas para a gestão de Centros de Custo.

Este blueprint define os endpoints para todas as operações CRUD
(Criar, Ler, Atualizar, Excluir) e funcionalidades de importação/exportação
para a entidade 'Centros de Custo', que faz parte dos Cadastros Mestres do sistema.
"""

import csv
import io
from typing import Any, Dict, List, Optional, Union

import pandas as pd
from firebase_admin import firestore
from flask import (
    Blueprint, Response, current_app, flash, redirect,
    render_template, request, url_for
)
from werkzeug.datastructures import FileStorage
from werkzeug.wrappers import Response as WerkzeugResponse

from app.auth.routes import login_required, role_required
from app.config import ALLOWED_EXTENSIONS  # Importa ALLOWED_EXTENSIONS para validação de upload
from app.services.firestore_service import (
    add_document, delete_document, get_all_documents,
    get_document, get_documents_by_query, update_document
)


cost_center_bp = Blueprint(
    'cost_centers',
    __name__,
    url_prefix='/cost_centers'
)


def allowed_file(filename: str) -> bool:
    """
    Verifica se a extensão do arquivo é permitida para upload.

    Args:
        filename (str): O nome do arquivo a ser verificado.

    Returns:
        bool: True se a extensão do arquivo for permitida, False caso contrário.
    """
    # Garante que o filename tem uma extensão antes de tentar o rsplit
    if '.' not in filename:
        return False
    return filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@cost_center_bp.route('/')
@login_required
@role_required('admin', 'viewer')
def list_cost_centers() -> Union[str, WerkzeugResponse]:
    """
    Exibe a lista de todos os Centros de Custo.

    Retorna:
        Union[str, WerkzeugResponse]: O template da lista de centros de custo
                                      renderizado ou um redirecionamento em
                                      caso de erro.
    """
    try:
        cost_centers: List[Dict[str, Any]] = get_all_documents('costCenters')
        return render_template('settings/cost_centers_list.html', cost_centers=cost_centers)
    except Exception as e:
        current_app.logger.error(f"Erro ao listar centros de custo: {e}", exc_info=True)
        flash("Ocorreu um erro crítico ao carregar os dados dos centros de custo.", "danger")
        return render_template('settings/cost_centers_list.html', cost_centers=[])


@cost_center_bp.route('/form', methods=['GET'])
@cost_center_bp.route('/form/<string:cost_center_id>', methods=['GET'])
@login_required
@role_required('admin')
def cost_center_form(cost_center_id: Optional[str] = None) -> Union[str, WerkzeugResponse]:
    """
    Exibe um formulário para adicionar ou editar um Centro de Custo.

    Args:
        cost_center_id (Optional[str]): O ID do centro de custo a ser editado.
                                        Se None, exibe um formulário em branco.

    Retorna:
        Union[str, WerkzeugResponse]: O template do formulário renderizado ou um
                                      redirecionamento se o ID não for encontrado.
    """
    try:
        cost_center: Dict[str, Any] = {}
        if cost_center_id:
            cost_center = get_document('costCenters', cost_center_id)
            if not cost_center:
                flash('Centro de Custo não encontrado.', 'danger')
                return redirect(url_for('cost_centers.list_cost_centers'))

        return render_template('settings/cost_center_form.html', cost_center=cost_center)
    except Exception as e:
        current_app.logger.error(
            f"Erro ao carregar formulário de centro de custo para ID '{cost_center_id}': {e}",
            exc_info=True
        )
        flash("Ocorreu um erro ao carregar o formulário do centro de custo.", "danger")
        return redirect(url_for('cost_centers.list_cost_centers'))


@cost_center_bp.route('/save/', methods=['POST'])
@cost_center_bp.route('/save/<string:cost_center_id>', methods=['POST'])
@login_required
@role_required('admin')
def save_cost_center(cost_center_id: Optional[str] = None) -> WerkzeugResponse:
    """
    Processa a submissão do formulário para criar ou atualizar um Centro de Custo.

    Args:
        cost_center_id (Optional[str]): O ID do centro de custo a ser atualizado.
                                        Se None, cria um novo.

    Retorna:
        WerkzeugResponse: Um redirecionamento para a lista de centros de custo.
    """
    try:
        form_data: Dict[str, Any] = request.form

        # Validação de campo obrigatório
        name: Optional[str] = form_data.get('name')
        if not name or not name.strip():
            flash('O nome do Centro de Custo é obrigatório.', 'danger')
            # Renderiza o formulário novamente com os dados submetidos para o usuário corrigir
            return render_template('settings/cost_center_form.html', cost_center=dict(form_data))

        data_to_save: Dict[str, Any] = {'name': name.strip()}

        # Lógica para o campo opcional 'description'
        description: Optional[str] = form_data.get('description')
        if description and description.strip():
            data_to_save['description'] = description.strip()
        elif cost_center_id:  # Se estiver atualizando e o campo foi esvaziado
            data_to_save['description'] = firestore.DELETE_FIELD
        # Caso contrário (criando e sem descrição, ou atualizando e já era None/vazio), não faz nada.

        if cost_center_id:
            data_to_save['updatedAt'] = firestore.SERVER_TIMESTAMP
            update_document('costCenters', cost_center_id, data_to_save)
            flash(f'Centro de Custo "{data_to_save["name"]}" atualizado com sucesso!', 'success')
        else:
            data_to_save['createdAt'] = firestore.SERVER_TIMESTAMP
            data_to_save['updatedAt'] = firestore.SERVER_TIMESTAMP
            # Omitir campos que são firestore.DELETE_FIELD na criação
            final_data = {k: v for k, v in data_to_save.items() if v is not firestore.DELETE_FIELD}
            add_document('costCenters', final_data)
            flash(f'Centro de Custo "{data_to_save["name"]}" criado com sucesso!', 'success')

    except Exception as e:
        current_app.logger.error(f"Erro ao salvar centro de custo: {e}", exc_info=True)
        flash("Ocorreu um erro inesperado ao salvar o centro de custo.", "danger")

    return redirect(url_for('cost_centers.list_cost_centers'))


@cost_center_bp.route('/delete/<string:cost_center_id>', methods=['POST'])
@login_required
@role_required('admin')
def delete_cost_center(cost_center_id: str) -> WerkzeugResponse:
    """
    Exclui um Centro de Custo, após verificar se não há dependências.

    Args:
        cost_center_id (str): O ID do centro de custo a ser excluído.

    Retorna:
        WerkzeugResponse: Um redirecionamento para a lista de centros de custo.
    """
    try:
        # Verificação de dependência: impede a exclusão se estiver em uso.
        # Verifica se o centro de custo está associado a setores
        dependent_sectors = get_documents_by_query('sectors', 'associatedCostCenterId', '==', cost_center_id)
        if dependent_sectors:
            flash(
                'Este Centro de Custo não pode ser excluído pois está associado a um ou mais setores.',
                'danger'
            )
            return redirect(url_for('cost_centers.list_cost_centers'))

        # Adicionar verificação se o centro de custo está associado a ativos
        # Supondo que ativos têm um campo 'assignedCostCenterId'
        dependent_assets = get_documents_by_query('assets', 'assignedCostCenterId', '==', cost_center_id)
        if dependent_assets:
            flash(
                'Este Centro de Custo não pode ser excluído pois está associado a um ou mais ativos.',
                'danger'
            )
            return redirect(url_for('cost_centers.list_cost_centers'))

        cost_center = get_document('costCenters', cost_center_id)
        if not cost_center:
            flash('Centro de Custo não encontrado.', 'danger')
        else:
            delete_document('costCenters', cost_center_id)
            flash(f'Centro de Custo "{cost_center.get("name", "N/A")}" excluído com sucesso!', 'success')

    except Exception as e:
        current_app.logger.error(f"Erro ao excluir centro de custo {cost_center_id}: {e}", exc_info=True)
        flash('Ocorreu um erro ao excluir o centro de custo.', 'danger')

    return redirect(url_for('cost_centers.list_cost_centers'))


@cost_center_bp.route('/import', methods=['GET', 'POST'])
@login_required
@role_required('admin')
def import_cost_centers_csv() -> Union[str, WerkzeugResponse]:
    """
    Gerencia o upload e processamento de um arquivo CSV para importação em massa de Centros de Custo.
    Valida, mapeia e adiciona/atualiza centros de custo no Firestore.

    Retorna:
        Union[str, WerkzeugResponse]: O HTML do formulário de importação ou um redirecionamento
                                      com feedback após o processamento.
    """
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('Nenhum arquivo enviado.', 'danger')
            return redirect(request.url)

        file: FileStorage = request.files['file']
        if file.filename == '':
            flash('Nenhum arquivo selecionado.', 'danger')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            try:
                # pandas reads CSV, assuming semicolon delimiter and 'latin1' encoding for broader compatibility
                df = pd.read_csv(io.StringIO(file.stream.read().decode('latin1')), delimiter=';')

                # Define mapping from CSV headers to Firestore field names (camelCase)
                column_mapping = {
                    'name': 'name',
                    'description': 'description'
                    # Adicione outros campos se o template de importação tiver mais
                }
                df.rename(columns=column_mapping, inplace=True)

                imported_count = 0
                updated_count = 0
                errors: List[str] = []

                for index, row in df.iterrows():
                    cost_center_data: Dict[str, Any] = {}
                    try:
                        name_from_csv: Optional[str] = str(row.get('name', '')).strip()

                        # Basic validation
                        if not name_from_csv:
                            errors.append(f"Linha {index + 2}: Nome do Centro de Custo é obrigatório.")
                            continue

                        cost_center_data['name'] = name_from_csv

                        # Handle optional description
                        description_from_csv: Optional[str] = str(row.get('description', '')).strip()
                        if description_from_csv:
                            cost_center_data['description'] = description_from_csv
                        else:
                            # Se a descrição estiver vazia no CSV, não a adiciona ao dicionário
                            # para que Firestore não crie um campo vazio.
                            # Para updates, se precisar remover, a lógica seria mais complexa
                            # e exigiria buscar o CC existente antes.
                            pass

                        # Check if a cost center with this name already exists for update logic
                        existing_cost_centers = get_documents_by_query('costCenters', 'name', '==', name_from_csv)
                        
                        if existing_cost_centers:
                            # Assume o primeiro encontrado para atualização.
                            # Para múltiplos resultados, seria necessário uma desambiguação.
                            existing_id = existing_cost_centers[0]['id']
                            update_document('costCenters', existing_id, {
                                'name': cost_center_data['name'],
                                'description': cost_center_data.get('description', firestore.DELETE_FIELD), # Atualiza ou remove descrição
                                'updatedAt': firestore.SERVER_TIMESTAMP
                            })
                            updated_count += 1
                        else:
                            cost_center_data['createdAt'] = firestore.SERVER_TIMESTAMP
                            cost_center_data['updatedAt'] = firestore.SERVER_TIMESTAMP
                            add_document('costCenters', cost_center_data)
                            imported_count += 1

                    except Exception as e:
                        errors.append(f"Linha {index + 2} ({row.get('name', 'N/A')}): Erro ao processar: {e}")
                        current_app.logger.error(
                            f"Erro ao importar centro de custo na linha {index + 2}: {e}", exc_info=True
                        )

                if imported_count > 0:
                    flash(f'{imported_count} centros de custo novos importados com sucesso!', 'success')
                if updated_count > 0:
                    flash(f'{updated_count} centros de custo existentes atualizados com sucesso!', 'info')
                if errors:
                    flash(f'Total de erros: {len(errors)}. Verifique o log para detalhes.', 'warning')
                    for error_msg in errors[:5]:  # Mostra os primeiros 5 erros no flash
                        flash(f'Erro: {error_msg}', 'warning')
                if imported_count == 0 and updated_count == 0 and not errors:
                    flash('Nenhum centro de custo foi importado ou atualizado. Verifique o formato do arquivo.', 'info')

            except pd.errors.EmptyDataError:
                flash('O arquivo CSV está vazio.', 'danger')
            except pd.errors.ParserError:
                flash('Erro ao analisar o arquivo CSV. Verifique o delimitador (ponto e vírgula) e o formato.', 'danger')
            except Exception as e:
                current_app.logger.error(f"Erro geral na importação de centros de custo: {e}", exc_info=True)
                flash(f'Ocorreu um erro inesperado durante a importação: {e}', 'danger')

        else:
            flash('Tipo de arquivo não permitido. Apenas ficheiros CSV são aceites.', 'danger')

        return redirect(url_for('cost_centers.list_cost_centers'))
    return render_template('settings/cost_center_import_form.html')


@cost_center_bp.route('/export/csv') # Rota adicionada para exportação
@login_required
@role_required('admin', 'viewer')
def export_cost_centers_csv() -> Union[Response, WerkzeugResponse]:
    """
    Exporta todos os Centros de Custo para um ficheiro CSV detalhado.

    Retorna:
        Union[Response, WerkzeugResponse]: Uma resposta HTTP contendo o arquivo CSV
                                           ou um redirecionamento em caso de erro.
    """
    try:
        all_cost_centers: List[Dict[str, Any]] = get_all_documents('costCenters')

        output = io.StringIO()
        writer = csv.writer(output, delimiter=';')

        headers = ['ID', 'Nome', 'Descrição']
        writer.writerow(headers)

        for cc in all_cost_centers:
            row = [
                cc.get('id', ''),
                cc.get('name', ''),
                cc.get('description', '')
            ]
            writer.writerow(row)

        output.seek(0)
        return Response(
            output.getvalue(),
            mimetype="text/csv",
            headers={"Content-Disposition": "attachment;filename=export_centros_custo.csv"}
        )
    except Exception as e:
        current_app.logger.error(f"Erro ao exportar centros de custo para CSV: {e}", exc_info=True)
        flash('Ocorreu um erro ao exportar os centros de custo.', 'danger')
        return redirect(url_for('cost_centers.list_cost_centers'))


@cost_center_bp.route('/export/template/csv')
@login_required
@role_required('admin')
def download_cost_center_template_csv() -> Response:
    """
    Fornece um template CSV para download, com as colunas esperadas para importação
    de Centros de Custo.

    Retorna:
        Response: Uma resposta HTTP contendo o template CSV.
    """
    output = io.StringIO()
    writer = csv.writer(output, delimiter=';')

    headers = ['name', 'description']
    writer.writerow(headers)
    writer.writerow(['TI-Infra', 'Centro de Custo para infraestrutura de TI'])
    writer.writerow(['ADM-Geral', 'Centro de Custo para despesas administrativas gerais'])

    output.seek(0)
    return Response(
        output.getvalue(),
        mimetype="text/csv",
        headers={"Content-Disposition": "attachment;filename=template_import_centros_custo.csv"}
    )