"""
Módulo de rotas para a gestão de Despesas.

Este blueprint define os endpoints para todas as operações CRUD
(Criar, Ler, Atualizar, Excluir) para a entidade 'Despesas',
incluindo a integração com 'Tipos de Despesas', 'Setores', 'Unidades' e 'Centros de Custo'.
"""

import csv
import io
import datetime # <-- CORREÇÃO: Adicionado o import de datetime
from typing import Any, Dict, List, Optional, Union

import pandas as pd
from firebase_admin import firestore
from flask import (Blueprint, Response, current_app, flash, redirect,
                   render_template, request, url_for)
from werkzeug.datastructures import FileStorage
from werkzeug.wrappers import Response as WerkzeugResponse

from app.auth.routes import login_required, role_required
from app.config import ALLOWED_EXTENSIONS
from app.models.expense import Expense
from app.services.firestore_service import (add_document, delete_document,
                                            get_all_documents, get_document,
                                            get_documents_by_query,
                                            update_document)
from app.models.expense_type import ExpenseType # Importa ExpenseType para mapeamento de nomes


expense_bp = Blueprint('expenses', __name__, url_prefix='/expenses')


# --- Funções Auxiliares ---


def _prepare_expense_for_template(expense_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Prepara os dados de uma despesa para exibição segura no template HTML.

    Formata campos como datas para o formato esperado por inputs HTML.

    Args:
        expense_data (Dict[str, Any]): Um dicionário contendo os dados da despesa.

    Returns:
        Dict[str, Any]: O dicionário de dados da despesa com campos formatados.
    """
    if not expense_data:
        return {}

    # Formata a data de referência para preencher o campo <input type="date"> (AAAA-MM-DD)
    # Assumindo que referenceDate pode ser um objeto datetime.datetime
    if 'referenceDate' in expense_data and isinstance(expense_data.get('referenceDate'), datetime.datetime):
        expense_data['referenceDate'] = expense_data['referenceDate'].strftime('%Y-%m-%d')
    
    # Assegura que o value é tratado como float para exibição
    if 'value' in expense_data and expense_data['value'] is not None:
        try:
            expense_data['value'] = float(expense_data['value'])
        except (ValueError, TypeError):
            current_app.logger.warning(f"Valor de despesa inválido ao preparar para template: {expense_data.get('value')}")
            expense_data['value'] = 0.0 # Define um default seguro

    return expense_data


def _build_expense_context(
    expense_data: Dict[str, Any] = None, expense_id: Optional[str] = None
) -> Dict[str, Any]:
    """
    Constrói o dicionário de contexto completo para o formulário de despesa.

    Inclui dados da despesa (se houver), e listas de opções para dropdowns
    como setores, unidades, centros de custo e tipos de despesa.

    Args:
        expense_data (Dict[str, Any], optional): Dados da despesa para pré-preenchimento.
                                                 Padrão para dicionário vazio.
        expense_id (Optional[str], optional): ID da despesa, se for uma edição.

    Returns:
        Dict[str, Any]: Dicionário de contexto com todos os dados necessários
                        para renderizar o formulário.
    """
    expense_data = expense_data if expense_data is not None else {}
    try:
        sectors = get_all_documents('sectors')
        units = get_all_documents('units')
        cost_centers = get_all_documents('costCenters')
        expense_types = get_all_documents('expenseTypes')

        return {
            'expense': expense_data,
            'expense_id': expense_id,
            'sectors': sectors,
            'units': units,
            'cost_centers': cost_centers,
            'expense_types': expense_types
        }
    except Exception as e:
        current_app.logger.error(
            f"Erro ao construir contexto para formulário de despesa: {e}",
            exc_info=True
        )
        flash('Não foi possível carregar as opções do formulário.', 'danger')
        return {
            'expense': expense_data,
            'expense_id': expense_id,
            'sectors': [], 'units': [], 'cost_centers': [], 'expense_types': []
        }


def _parse_form_date(date_string: Optional[str]) -> Optional[datetime.datetime]:
    """
    Converte uma string 'AAAA-MM-DD' de um formulário para um objeto datetime UTC.

    Args:
        date_string (Optional[str]): A string da data no formato 'YYYY-MM-DD'.

    Returns:
        Optional[datetime.datetime]: O objeto datetime correspondente em UTC,
                                     ou None se a string for inválida ou vazia.
    """
    if not date_string:
        return None
    try:
        return datetime.datetime.strptime(date_string, '%Y-%m-%d').replace(tzinfo=datetime.timezone.utc)
    except (ValueError, TypeError) as e:
        current_app.logger.warning(f"Formato de data inválido recebido: '{date_string}'. Erro: {e}")
        return None


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


# --- Rotas do Módulo de Despesas ---


@expense_bp.route('/')
@login_required
@role_required('admin', 'viewer')
def list_expenses() -> Union[str, WerkzeugResponse]:
    """
    Exibe a lista de todas as despesas.

    Enriquece os dados das despesas com nomes de setores, unidades, centros de custo
    e tipos de despesas para exibição na tabela.

    Retorna:
        Union[str, WerkzeugResponse]: O template da lista de despesas renderizado
                                      ou um redirecionamento em caso de erro.
    """
    try:
        expenses_data: List[Dict[str, Any]] = get_all_documents('expenses')

        sectors_map = {s['id']: s.get('name', 'N/A') for s in get_all_documents('sectors')}
        units_map = {u['id']: u.get('name', 'N/A') for u in get_all_documents('units')}
        cost_centers_map = {cc['id']: cc.get('name', 'N/A') for cc in get_all_documents('costCenters')}
        expense_types_map = {et['id']: et.get('name', 'N/A') for et in get_all_documents('expenseTypes')}


        expenses_for_template: List[Dict[str, Any]] = []
        for expense in expenses_data:
            expense_obj = Expense.from_dict(expense, expense.get('id'))
            
            display_expense = expense_obj.to_dict()
            display_expense['id'] = expense_obj.id

            display_expense['sectorName'] = sectors_map.get(display_expense.get('sectorId'), 'N/A')
            display_expense['unitName'] = units_map.get(display_expense.get('unitId'), 'N/A')
            display_expense['costCenterName'] = cost_centers_map.get(display_expense.get('costCenterId'), 'N/A')
            display_expense['expenseTypeName'] = expense_types_map.get(display_expense.get('expenseTypeId'), 'N/A')

            if isinstance(expense_obj.referenceMonth, int) and isinstance(expense_obj.referenceYear, int):
                try:
                    ref_date = datetime.datetime(expense_obj.referenceYear, expense_obj.referenceMonth, 1)
                    display_expense['referencePeriodFormatted'] = ref_date.strftime('%m/%Y')
                except ValueError:
                    display_expense['referencePeriodFormatted'] = 'Data Inválida'
            else:
                display_expense['referencePeriodFormatted'] = 'N/A'

            if isinstance(display_expense.get('value'), (float, int)):
                display_expense['valueFormatted'] = f"{display_expense['value']:.2f}".replace('.', ',')
            else:
                display_expense['valueFormatted'] = '0,00'
            
            expenses_for_template.append(display_expense)

        return render_template('expenses/list.html', expenses=expenses_for_template)
    except Exception as e:
        current_app.logger.error(f"Erro ao listar despesas: {e}", exc_info=True)
        flash("Ocorreu um erro ao carregar as despesas.", "danger")
        return render_template('expenses/list.html', expenses=[])


@expense_bp.route('/form', methods=['GET'])
@expense_bp.route('/form/<string:expense_id>', methods=['GET'])
@login_required
@role_required('admin')
def expense_form(expense_id: Optional[str] = None) -> Union[str, WerkzeugResponse]:
    """
    Exibe o formulário para adicionar ou editar uma despesa.
    """
    try:
        expense: Dict[str, Any] = {}
        if expense_id:
            expense = get_document('expenses', expense_id)
            if not expense:
                flash('Despesa não encontrada.', 'danger')
                return redirect(url_for('expenses.list_expenses'))
        
        expense_for_template = _prepare_expense_for_template(expense)
        context = _build_expense_context(expense_for_template, expense_id)
        
        return render_template('expenses/form.html', **context)
    except Exception as e:
        current_app.logger.error(f"Erro ao carregar formulário de despesa para ID '{expense_id}': {e}", exc_info=True)
        flash("Ocorreu um erro ao carregar o formulário da despesa.", "danger")
        return redirect(url_for('expenses.list_expenses'))


@expense_bp.route('/save/', methods=['POST'])
@expense_bp.route('/save/<string:expense_id>', methods=['POST'])
@login_required
@role_required('admin')
def save_expense(expense_id: Optional[str] = None) -> WerkzeugResponse:
    """
    Salva uma nova despesa ou atualiza uma existente no Firestore.
    """
    try:
        form_data: Dict[str, Any] = request.form

        required_fields_map = {
            'expenseTypeId': 'Tipo de Despesa',
            'value': 'Valor',
            'referenceDate': 'Data de Referência',
            'sectorId': 'Setor',
            'unitId': 'Unidade',
            'costCenterId': 'Centro de Custo'
        }
        missing_fields = []
        for field, display_name in required_fields_map.items():
            if field == 'referenceDate':
                if not form_data.get(field):
                    missing_fields.append(display_name)
            elif not form_data.get(field) or (isinstance(form_data.get(field), str) and not form_data.get(field).strip()):
                missing_fields.append(display_name)
        
        if missing_fields:
            flash(f"Os seguintes campos obrigatórios não foram preenchidos: {', '.join(missing_fields)}.", 'danger')
            context = _build_expense_context({key: val for key, val in form_data.items()}, expense_id)
            if 'referenceDate' in context['expense']:
                context['expense']['referenceDate'] = context['expense']['referenceDate']
            return render_template('expenses/form.html', **context)

        try:
            expense_value = float(form_data.get('value', '0').replace(',', '.'))
        except ValueError:
            flash('O campo "Valor" deve ser um número válido.', 'danger')
            context = _build_expense_context({key: val for key, val in form_data.items()}, expense_id)
            return render_template('expenses/form.html', **context)
            
        reference_date_str = form_data.get('referenceDate')
        reference_month = None
        reference_year = None
        if reference_date_str:
            parsed_date = _parse_form_date(reference_date_str)
            if parsed_date:
                reference_month = parsed_date.month
                reference_year = parsed_date.year
            else:
                flash('Formato da "Data de Referência" inválido. Use AAAA-MM-DD.', 'danger')
                context = _build_expense_context({key: val for key, val in form_data.items()}, expense_id)
                return render_template('expenses/form.html', **context)
        else:
            flash('O campo "Data de Referência" é obrigatório.', 'danger')
            context = _build_expense_context({key: val for key, val in form_data.items()}, expense_id)
            return render_template('expenses/form.html', **context)


        expense_obj = Expense(
            value=expense_value,
            reference_month=reference_month,
            reference_year=reference_year,
            expense_type_id=form_data.get('expenseTypeId'),
            sector_id=form_data.get('sectorId'),
            unit_id=form_data.get('unitId'),
            cost_center_id=form_data.get('costCenterId'),
            description=form_data.get('description')
        )
        data_to_save: Dict[str, Any] = expense_obj.to_dict()

        if expense_id:
            data_to_save['updatedAt'] = firestore.SERVER_TIMESTAMP
            update_document('expenses', expense_id, data_to_save)
            flash('Despesa atualizada com sucesso!', 'success')
        else:
            data_to_save['createdAt'] = firestore.SERVER_TIMESTAMP
            data_to_save['updatedAt'] = firestore.SERVER_TIMESTAMP
            add_document('expenses', data_to_save)
            flash('Despesa registrada com sucesso!', 'success')

    except Exception as e:
        current_app.logger.error(f"Erro inesperado ao salvar despesa: {e}", exc_info=True)
        flash('Ocorreu um erro inesperado ao salvar a despesa.', 'danger')
    
    return redirect(url_for('expenses.list_expenses'))


@expense_bp.route('/delete/<string:expense_id>', methods=['POST'])
@login_required
@role_required('admin')
def delete_expense(expense_id: str) -> WerkzeugResponse:
    """
    Exclui uma despesa.
    """
    try:
        expense = get_document('expenses', expense_id)
        if not expense:
            flash('Despesa não encontrada para exclusão.', 'danger')
        else:
            delete_document('expenses', expense_id)
            flash(f'Despesa (Valor: {expense.get("value", "N/A")}) excluída com sucesso!', 'success')
    except Exception as e:
        current_app.logger.error(f"Erro ao excluir despesa {expense_id}: {e}", exc_info=True)
        flash('Ocorreu um erro ao excluir a despesa.', 'danger')
        
    return redirect(url_for('expenses.list_expenses'))

# --- ROTAS DE IMPORTAÇÃO E EXPORTAÇÃO PARA DESPESAS ---

@expense_bp.route('/export/csv')
@login_required
@role_required('admin', 'viewer')
def export_expenses_csv() -> Union[Response, WerkzeugResponse]:
    """
    Exporta todas as Despesas para um ficheiro CSV detalhado.

    Inclui informações mapeadas de setores, unidades, centros de custo e tipos de despesas.
    """
    try:
        expenses_data: List[Dict[str, Any]] = get_all_documents('expenses')

        sectors_map = {s['id']: s.get('name', 'N/A') for s in get_all_documents('sectors')}
        units_map = {u['id']: u.get('name', 'N/A') for u in get_all_documents('units')}
        cost_centers_map = {cc['id']: cc.get('name', 'N/A') for cc in get_all_documents('costCenters')}
        expense_types_map = {et['id']: et.get('name', 'N/A') for et in get_all_documents('expenseTypes')}

        output = io.StringIO()
        writer = csv.writer(output, delimiter=';')

        headers = [
            'ID', 'Tipo de Despesa', 'Valor', 'Mês Referência', 'Ano Referência',
            'Setor', 'Unidade', 'Centro de Custo', 'Descrição'
        ]
        writer.writerow(headers)

        for expense in expenses_data:
            expense_obj = Expense.from_dict(expense, expense.get('id'))
            
            row = [
                expense_obj.id,
                expense_types_map.get(expense_obj.expenseTypeId, 'N/A'),
                f"{expense_obj.value:.2f}".replace('.', ','),
                expense_obj.referenceMonth,
                expense_obj.referenceYear,
                sectors_map.get(expense_obj.sectorId, 'N/A'),
                units_map.get(expense_obj.unitId, 'N/A'),
                cost_centers_map.get(expense_obj.costCenterId, 'N/A'),
                expense_obj.description or ''
            ]
            writer.writerow(row)

        output.seek(0)
        return Response(
            output.getvalue(),
            mimetype="text/csv",
            headers={"Content-Disposition": "attachment;filename=export_despesas.csv"}
        )
    except Exception as e:
        current_app.logger.error(f"Erro ao exportar despesas para CSV: {e}", exc_info=True)
        flash('Ocorreu um erro ao exportar as despesas.', 'danger')
        return redirect(url_for('expenses.list_expenses'))


@expense_bp.route('/import', methods=['GET', 'POST'])
@login_required
@role_required('admin')
def import_expenses_csv() -> Union[str, WerkzeugResponse]:
    """
    Gerencia o upload e processamento de um arquivo CSV para importação em massa de Despesas.
    Valida, mapeia e adiciona/atualiza despesas no Firestore.
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

                sectors_by_name = {s.get('name', '').lower(): s['id'] for s in get_all_documents('sectors')}
                units_by_name = {u.get('name', '').lower(): u['id'] for u in get_all_documents('units')}
                cost_centers_by_name = {cc.get('name', '').lower(): cc['id'] for cc in get_all_documents('costCenters')}
                expense_types_by_name = {et.get('name', '').lower(): et['id'] for et in get_all_documents('expenseTypes')}


                imported_count = 0
                updated_count = 0
                errors: List[str] = []

                for index, row in df.iterrows():
                    try:
                        expense_type_name_csv: Optional[str] = str(row.get('Tipo de Despesa', '')).strip()
                        value_csv_str: Optional[str] = str(row.get('Valor', '0')).strip()
                        reference_date_csv_str: Optional[str] = str(row.get('Data Referência', '')).strip()
                        sector_name_csv: Optional[str] = str(row.get('Setor', '')).strip()

                        unit_name_csv: Optional[str] = str(row.get('Unidade', '')).strip()
                        cost_center_name_csv: Optional[str] = str(row.get('Centro de Custo', '')).strip()
                        description_csv: Optional[str] = str(row.get('Descrição', '')).strip() or None


                        # --- Validações e Mapeamentos ---
                        if not expense_type_name_csv:
                            errors.append(f"Linha {index + 2}: 'Tipo de Despesa' é obrigatório.")
                            continue
                        expense_type_id = expense_types_by_name.get(expense_type_name_csv.lower())
                        if not expense_type_id:
                            errors.append(f"Linha {index + 2}: Tipo de Despesa '{expense_type_name_csv}' não encontrado.")
                            continue

                        try:
                            value = float(value_csv_str.replace(',', '.'))
                        except (ValueError, TypeError):
                            errors.append(f"Linha {index + 2}: 'Valor' '{value_csv_str}' é inválido.")
                            continue

                        parsed_ref_date = None
                        if reference_date_csv_str:
                            try:
                                parsed_ref_date = datetime.datetime.strptime(reference_date_csv_str, '%d/%m/%Y').replace(tzinfo=datetime.timezone.utc)
                            except ValueError:
                                errors.append(f"Linha {index + 2}: 'Data Referência' '{reference_date_csv_str}' com formato inválido. Use DD/MM/AAAA.")
                                continue
                        else:
                            errors.append(f"Linha {index + 2}: 'Data Referência' é obrigatória.")
                            continue
                        
                        if not parsed_ref_date:
                             errors.append(f"Linha {index + 2}: 'Data Referência' inválida após parsing.")
                             continue

                        sector_id = sectors_by_name.get(sector_name_csv.lower())
                        if not sector_id:
                            errors.append(f"Linha {index + 2}: Setor '{sector_name_csv}' não encontrado.")
                            continue

                        unit_id = units_by_name.get(unit_name_csv.lower()) if unit_name_csv else None
                        cost_center_id = cost_centers_by_name.get(cost_center_name_csv.lower()) if cost_center_name_csv else None

                        expense_obj = Expense(
                            value=value,
                            reference_month=parsed_ref_date.month,
                            reference_year=parsed_ref_date.year,
                            expense_type_id=expense_type_id,
                            sector_id=sector_id,
                            unit_id=unit_id,
                            cost_center_id=cost_center_id,
                            description=description_csv
                        )
                        data_to_save: Dict[str, Any] = expense_obj.to_dict()

                        data_to_save['createdAt'] = firestore.SERVER_TIMESTAMP
                        data_to_save['updatedAt'] = firestore.SERVER_TIMESTAMP
                        add_document('expenses', data_to_save)
                        imported_count += 1

                    except Exception as e:
                        errors.append(f"Linha {index + 2} (Tipo: {row.get('Tipo de Despesa', 'N/A')}): Erro ao processar: {e}")
                        current_app.logger.error(
                            f"Erro ao importar despesa na linha {index + 2}: {e}", exc_info=True
                        )

                if imported_count > 0:
                    flash(f'{imported_count} despesas novas importadas com sucesso!', 'success')
                if updated_count > 0:
                    flash(f'{updated_count} despesas existentes atualizadas com sucesso!', 'info')
                if errors:
                    flash(f'Total de erros: {len(errors)}. Verifique o log para detalhes.', 'warning')
                    for error_msg in errors[:5]:
                        flash(f'Erro: {error_msg}', 'warning')
                if imported_count == 0 and updated_count == 0 and not errors:
                    flash('Nenhuma despesa foi importada ou atualizada. Verifique o formato do arquivo.', 'info')

            except pd.errors.EmptyDataError:
                flash('O arquivo CSV está vazio.', 'danger')
            except pd.errors.ParserError:
                flash('Erro ao analisar o arquivo CSV. Verifique o delimitador (ponto e vírgula) e o formato.', 'danger')
            except Exception as e:
                current_app.logger.error(f"Erro geral na importação de despesas: {e}", exc_info=True)
                flash(f'Ocorreu um erro inesperado durante a importação: {e}', 'danger')

        else:
            flash('Tipo de arquivo não permitido. Apenas ficheiros CSV são aceites.', 'danger')

        return redirect(url_for('expenses.list_expenses'))
    return render_template('expenses/import_form.html')


@expense_bp.route('/export/template/csv')
@login_required
@role_required('admin')
def download_expense_template_csv() -> Response:
    """
    Fornece um template CSV para download, com as colunas esperadas para importação de Despesas.
    """
    output = io.StringIO()
    writer = csv.writer(output, delimiter=';')

    headers = [
        'Tipo de Despesa', 'Valor', 'Data Referência', 'Setor',
        'Unidade', 'Centro de Custo', 'Descrição'
    ]
    writer.writerow(headers)
    writer.writerow([
        'Telefonia', '150.75', '29/06/2025', 'Tecnologia da Informação',
        'Matriz', 'TI-Infra', 'Conta mensal de internet e telefone'
    ])
    writer.writerow([
        'Aluguel Impressora', '80.00', '29/05/2025', 'Recursos Humanos',
        '', '', 'Aluguel de impressora para o setor de RH'
    ])
    output.seek(0)
    return Response(
        output.getvalue(),
        mimetype="text/csv",
        headers={"Content-Disposition": "attachment;filename=template_import_despesas.csv"}
    )