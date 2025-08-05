"""
Módulo de rotas para a gestão de Tipos de Despesas.

Este blueprint define os endpoints para todas as operações CRUD
(Criar, Ler, Atualizar, Excluir) e funcionalidades de importação/exportação
para a entidade 'Tipo de Despesa'.
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
from app.config import ALLOWED_EXTENSIONS  # Para validação de upload de CSV
from app.models.expense_type import ExpenseType  # Importa o modelo ExpenseType
from app.services.firestore_service import (
    add_document, delete_document, get_all_documents,
    get_document, get_documents_by_query, update_document
)


expense_type_bp = Blueprint(
    'expense_types',
    __name__,
    url_prefix='/expense_types'
)


def allowed_file(filename: str) -> bool:
    """
    Verifica se a extensão do arquivo é permitida para upload.

    Args:
        filename (str): O nome do arquivo a ser verificado.

    Returns:
        bool: True se a extensão do arquivo for permitida, False caso contrário.
    """
    if '.' not in filename:
        return False
    return filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@expense_type_bp.route('/')
@login_required
@role_required('admin', 'viewer')
def list_expense_types() -> Union[str, WerkzeugResponse]:
    """
    Exibe a lista de todos os Tipos de Despesas.

    Retorna:
        Union[str, WerkzeugResponse]: O template da lista de tipos de despesas
                                      renderizado ou um redirecionamento em
                                      caso de erro.
    """
    try:
        # Pega todos os documentos da coleção 'expenseTypes'
        expense_types_data: List[Dict[str, Any]] = get_all_documents('expenseTypes')
        # Opcional: converter para objetos ExpenseType se houver necessidade de métodos do objeto
        # expense_types = [ExpenseType.from_dict(data, data['id']) for data in expense_types_data]
        return render_template('settings/expense_types_list.html', expense_types=expense_types_data)
    except Exception as e:
        current_app.logger.error(f"Erro ao listar tipos de despesas: {e}", exc_info=True)
        flash("Ocorreu um erro crítico ao carregar os dados dos tipos de despesas.", "danger")
        return render_template('settings/expense_types_list.html', expense_types=[])


@expense_type_bp.route('/form', methods=['GET'])
@expense_type_bp.route('/form/<string:expense_type_id>', methods=['GET'])
@login_required
@role_required('admin')
def expense_type_form(expense_type_id: Optional[str] = None) -> Union[str, WerkzeugResponse]:
    """
    Exibe um formulário para adicionar ou editar um Tipo de Despesa.

    Args:
        expense_type_id (Optional[str]): O ID do tipo de despesa a ser editado.
                                         Se None, exibe um formulário em branco.

    Retorna:
        Union[str, WerkzeugResponse]: O template do formulário renderizado ou um
                                      redirecionamento se o ID não for encontrado.
    """
    try:
        expense_type: Dict[str, Any] = {}
        if expense_type_id:
            expense_type = get_document('expenseTypes', expense_type_id)
            if not expense_type:
                flash('Tipo de Despesa não encontrado.', 'danger')
                return redirect(url_for('expense_types.list_expense_types'))

        return render_template('settings/expense_type_form.html', expense_type=expense_type)
    except Exception as e:
        current_app.logger.error(
            f"Erro ao carregar formulário de tipo de despesa para ID '{expense_type_id}': {e}",
            exc_info=True
        )
        flash("Ocorreu um erro ao carregar o formulário do tipo de despesa.", "danger")
        return redirect(url_for('expense_types.list_expense_types'))


@expense_type_bp.route('/save/', methods=['POST'])
@expense_type_bp.route('/save/<string:expense_type_id>', methods=['POST'])
@login_required
@role_required('admin')
def save_expense_type(expense_type_id: Optional[str] = None) -> WerkzeugResponse:
    """
    Processa a submissão do formulário para criar ou atualizar um Tipo de Despesa.

    Args:
        expense_type_id (Optional[str]): O ID do tipo de despesa a ser atualizado.
                                         Se None, cria um novo.

    Retorna:
        WerkzeugResponse: Um redirecionamento para a lista de tipos de despesas.
    """
    try:
        form_data: Dict[str, Any] = request.form

        # Validação de campo obrigatório
        name: Optional[str] = form_data.get('name')
        if not name or not name.strip():
            flash('O nome do Tipo de Despesa é obrigatório.', 'danger')
            # Renderiza o formulário novamente com os dados submetidos para o usuário corrigir
            return render_template('settings/expense_type_form.html', expense_type=dict(form_data))

        # Cria um objeto ExpenseType para garantir que os dados sigam o modelo
        expense_type_obj = ExpenseType(
            name=name.strip(),
            description=form_data.get('description', '').strip() or None, # Use None se estiver vazio
            id=expense_type_id # Se estiver editando, o ID já está presente
        )
        data_to_save: Dict[str, Any] = expense_type_obj.to_dict()

        # Adiciona timestamps de criação/atualização
        if expense_type_id:
            data_to_save['updatedAt'] = firestore.SERVER_TIMESTAMP
            update_document('expenseTypes', expense_type_id, data_to_save)
            flash(f'Tipo de Despesa "{data_to_save["name"]}" atualizado com sucesso!', 'success')
        else:
            data_to_save['createdAt'] = firestore.SERVER_TIMESTAMP
            data_to_save['updatedAt'] = firestore.SERVER_TIMESTAMP
            # Omitir campos que são firestore.DELETE_FIELD (se aplicável, embora não haja no ExpenseType atual)
            # Para o ExpenseType, o to_dict já filtra None, então não precisamos de firestore.DELETE_FIELD na criação
            add_document('expenseTypes', data_to_save)
            flash(f'Tipo de Despesa "{data_to_save["name"]}" criado com sucesso!', 'success')

    except Exception as e:
        current_app.logger.error(f"Erro ao salvar tipo de despesa: {e}", exc_info=True)
        flash("Ocorreu um erro inesperado ao salvar o tipo de despesa.", "danger")

    return redirect(url_for('expense_types.list_expense_types'))


@expense_type_bp.route('/delete/<string:expense_type_id>', methods=['POST'])
@login_required
@role_required('admin')
def delete_expense_type(expense_type_id: str) -> WerkzeugResponse:
    """
    Exclui um Tipo de Despesa, após verificar se não há dependências.

    Args:
        expense_type_id (str): O ID do tipo de despesa a ser excluído.

    Retorna:
        WerkzeugResponse: Um redirecionamento para a lista de tipos de despesas.
    """
    try:
        # Verificação de dependência: impede a exclusão se estiver em uso.
        # Ex: verificar se está associado a alguma 'Expense'
        dependent_expenses = get_documents_by_query('expenses', 'expenseTypeId', '==', expense_type_id)
        if dependent_expenses:
            flash(
                'Este Tipo de Despesa não pode ser excluído pois está associado a uma ou mais despesas registradas.',
                'danger'
            )
            return redirect(url_for('expense_types.list_expense_types'))

        expense_type = get_document('expenseTypes', expense_type_id)
        if not expense_type:
            flash('Tipo de Despesa não encontrado.', 'danger')
        else:
            delete_document('expenseTypes', expense_type_id)
            flash(f'Tipo de Despesa "{expense_type.get("name", "N/A")}" excluído com sucesso!', 'success')

    except Exception as e:
        current_app.logger.error(f"Erro ao excluir tipo de despesa {expense_type_id}: {e}", exc_info=True)
        flash('Ocorreu um erro ao excluir o tipo de despesa.', 'danger')

    return redirect(url_for('expense_types.list_expense_types'))


@expense_type_bp.route('/import', methods=['GET', 'POST'])
@login_required
@role_required('admin')
def import_expense_types_csv() -> Union[str, WerkzeugResponse]:
    """
    Gerencia o upload e processamento de um arquivo CSV para importação em massa de Tipos de Despesas.
    Valida, mapeia e adiciona/atualiza tipos de despesas no Firestore.

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
                df = pd.read_csv(io.StringIO(file.stream.read().decode('latin1')), delimiter=';')

                column_mapping = {
                    'name': 'name',
                    'description': 'description'
                }
                df.rename(columns=column_mapping, inplace=True)

                imported_count = 0
                updated_count = 0
                errors: List[str] = []

                for index, row in df.iterrows():
                    try:
                        name_from_csv: Optional[str] = str(row.get('name', '')).strip()

                        if not name_from_csv:
                            errors.append(f"Linha {index + 2}: Nome do Tipo de Despesa é obrigatório.")
                            continue

                        description_from_csv: Optional[str] = str(row.get('description', '')).strip() or None

                        # Cria um objeto ExpenseType para validação e serialização
                        expense_type_obj = ExpenseType(
                            name=name_from_csv,
                            description=description_from_csv
                        )
                        data_to_save: Dict[str, Any] = expense_type_obj.to_dict()

                        # Verifica se um tipo de despesa com este nome já existe para atualização
                        existing_expense_types = get_documents_by_query('expenseTypes', 'name', '==', name_from_csv)
                        
                        if existing_expense_types:
                            existing_id = existing_expense_types[0]['id']
                            update_document('expenseTypes', existing_id, {
                                'name': data_to_save['name'],
                                'description': data_to_save.get('description', firestore.DELETE_FIELD),
                                'updatedAt': firestore.SERVER_TIMESTAMP
                            })
                            updated_count += 1
                        else:
                            data_to_save['createdAt'] = firestore.SERVER_TIMESTAMP
                            data_to_save['updatedAt'] = firestore.SERVER_TIMESTAMP
                            add_document('expenseTypes', data_to_save)
                            imported_count += 1

                    except Exception as e:
                        errors.append(f"Linha {index + 2} ({row.get('name', 'N/A')}): Erro ao processar: {e}")
                        current_app.logger.error(
                            f"Erro ao importar tipo de despesa na linha {index + 2}: {e}", exc_info=True
                        )

                if imported_count > 0:
                    flash(f'{imported_count} tipos de despesas novos importados com sucesso!', 'success')
                if updated_count > 0:
                    flash(f'{updated_count} tipos de despesas existentes atualizados com sucesso!', 'info')
                if errors:
                    flash(f'Total de erros: {len(errors)}. Verifique o log para detalhes.', 'warning')
                    for error_msg in errors[:5]:
                        flash(f'Erro: {error_msg}', 'warning')
                if imported_count == 0 and updated_count == 0 and not errors:
                    flash('Nenhum tipo de despesa foi importado ou atualizado. Verifique o formato do arquivo.', 'info')

            except pd.errors.EmptyDataError:
                flash('O arquivo CSV está vazio.', 'danger')
            except pd.errors.ParserError:
                flash('Erro ao analisar o arquivo CSV. Verifique o delimitador (ponto e vírgula) e o formato.', 'danger')
            except Exception as e:
                current_app.logger.error(f"Erro geral na importação de tipos de despesas: {e}", exc_info=True)
                flash(f'Ocorreu um erro inesperado durante a importação: {e}', 'danger')

        else:
            flash('Tipo de arquivo não permitido. Apenas ficheiros CSV são aceites.', 'danger')

        return redirect(url_for('expense_types.list_expense_types'))
    return render_template('settings/expense_type_import_form.html')


@expense_type_bp.route('/export/csv')
@login_required
@role_required('admin', 'viewer')
def export_expense_types_csv() -> Union[Response, WerkzeugResponse]:
    """
    Exporta todos os Tipos de Despesas para um ficheiro CSV detalhado.

    Retorna:
        Union[Response, WerkzeugResponse]: Uma resposta HTTP contendo o arquivo CSV
                                           ou um redirecionamento em caso de erro.
    """
    try:
        all_expense_types: List[Dict[str, Any]] = get_all_documents('expenseTypes')

        output = io.StringIO()
        writer = csv.writer(output, delimiter=';')

        headers = ['ID', 'Nome', 'Descrição']
        writer.writerow(headers)

        for et in all_expense_types:
            row = [
                et.get('id', ''),
                et.get('name', ''),
                et.get('description', '')
            ]
            writer.writerow(row)

        output.seek(0)
        return Response(
            output.getvalue(),
            mimetype="text/csv",
            headers={"Content-Disposition": "attachment;filename=export_tipos_despesa.csv"}
        )
    except Exception as e:
        current_app.logger.error(f"Erro ao exportar tipos de despesas para CSV: {e}", exc_info=True)
        flash('Ocorreu um erro ao exportar os tipos de despesas.', 'danger')
        return redirect(url_for('expense_types.list_expense_types'))


@expense_type_bp.route('/export/template/csv')
@login_required
@role_required('admin')
def download_expense_type_template_csv() -> Response:
    """
    Fornece um template CSV para download, com as colunas esperadas para importação
    de Tipos de Despesas.

    Retorna:
        Response: Uma resposta HTTP contendo o template CSV.
    """
    output = io.StringIO()
    writer = csv.writer(output, delimiter=';')

    headers = ['name', 'description']
    writer.writerow(headers)
    writer.writerow(['Telefonia', 'Despesas com serviços de telefonia (fixa e móvel)'])
    writer.writerow(['Software', 'Custos de licenciamento de software'])
    writer.writerow(['Aluguel Impressora', 'Custo mensal de aluguel de impressoras'])

    output.seek(0)
    return Response(
        output.getvalue(),
        mimetype="text/csv",
        headers={"Content-Disposition": "attachment;filename=template_import_tipos_despesa.csv"}
    )