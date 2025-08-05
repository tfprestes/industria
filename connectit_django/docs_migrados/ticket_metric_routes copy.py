# app/routes/ticket_metric_routes.py

"""
Módulo de rotas para a gestão de Métricas de Chamados.

Define os endpoints para as operações CRUD e para a importação e
exportação de dados em formato CSV.
"""

import csv
import datetime
import io
import json
from typing import Any, Dict, List, Optional

import pandas as pd
from firebase_admin import firestore
from flask import (Blueprint, Response, current_app, flash, redirect,
                   render_template, request, session, url_for)
from werkzeug.wrappers import Response as WerkzeugResponse

from app.auth.routes import login_required, role_required
from app.services.firestore_service import (add_document, delete_document,
                                            get_all_documents, get_document,
                                            update_document)

ticket_metrics_bp = Blueprint(
    'ticket_metrics',
    __name__,
    url_prefix='/ticket-metrics'
)


def _get_form_context(metric_data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Constrói o dicionário de contexto para o formulário de métricas."""
    if metric_data is None:
        metric_data = {}
    try:
        return {
            'metric': metric_data,
            'sectors': get_all_documents('sectors'),
            'units': get_all_documents('units'),
            'cost_centers': get_all_documents('costCenters'),
            'months': [{'value': i, 'name': datetime.date(2000, i, 1).strftime('%B').capitalize()} for i in range(1, 13)],
            'years': list(range(datetime.datetime.now().year + 1, datetime.datetime.now().year - 5, -1))
        }
    except Exception as e:
        current_app.logger.error(f"Erro ao construir contexto para métricas: {e}", exc_info=True)
        flash("Falha ao carregar dados de apoio.", "danger")
        return {'metric': metric_data, 'sectors': [], 'units': [], 'cost_centers': [], 'months': [], 'years': []}


# --- Rotas CRUD ---

@ticket_metrics_bp.route('/')
@login_required
@role_required('admin', 'viewer')
def list_metrics() -> str:
    """Exibe a lista de todas as métricas de chamados."""
    try:
        all_metrics: List[Dict[str, Any]] = get_all_documents('ticketMetrics')
        context = _get_form_context()
        sectors_map = {s['id']: s.get('name', 'N/A') for s in context['sectors']}
        months_map = {m['value']: m['name'] for m in context['months']}

        for metric in all_metrics:
            metric['sectorName'] = sectors_map.get(metric.get('sectorId'), 'N/A')
            metric['monthName'] = months_map.get(int(metric.get('referenceMonth')), 'Inválido')

        return render_template('ticket_metrics/list.html', metrics=all_metrics)
    except Exception as e:
        current_app.logger.error(f"Erro ao listar métricas: {e}", exc_info=True)
        flash("Ocorreu um erro ao carregar as métricas.", "danger")
        return render_template('ticket_metrics/list.html', metrics=[])


@ticket_metrics_bp.route('/form', methods=['GET'])
@ticket_metrics_bp.route('/form/<string:metric_id>', methods=['GET'])
@login_required
@role_required('admin')
def metric_form(metric_id: Optional[str] = None) -> str | WerkzeugResponse:
    """Exibe um formulário unificado para adicionar ou editar uma métrica."""
    try:
        metric: Dict[str, Any] = get_document('ticketMetrics', metric_id) if metric_id else {}
        if metric_id and not metric:
            flash('Registo de métrica não encontrado.', 'danger')
            return redirect(url_for('ticket_metrics.list_metrics'))
        
        context = _get_form_context(metric)
        return render_template('ticket_metrics/form.html', **context)
    except Exception as e:
        current_app.logger.error(f"Erro ao carregar formulário de métrica: {e}", exc_info=True)
        flash("Ocorreu um erro ao carregar o formulário.", "danger")
        return redirect(url_for('ticket_metrics.list_metrics'))


@ticket_metrics_bp.route('/save/', methods=['POST'])
@ticket_metrics_bp.route('/save/<string:metric_id>', methods=['POST'])
@login_required
@role_required('admin')
def save_metric(metric_id: Optional[str] = None) -> WerkzeugResponse:
    """Salva uma nova métrica ou atualiza uma existente."""
    try:
        form_data: Dict[str, Any] = request.form
        required_fields = ['reference_month', 'reference_year', 'sector_id', 'unit_id', 'cost_center_id', 'count']
        if not all(form_data.get(f) for f in required_fields):
            flash('Todos os campos obrigatórios (*) devem ser preenchidos.', 'danger')
            context = _get_form_context(dict(form_data))
            return render_template('ticket_metrics/form.html', **context)

        data_to_save: Dict[str, Any] = {
            'referenceMonth': int(form_data.get('reference_month')),
            'referenceYear': int(form_data.get('reference_year')),
            'sectorId': form_data.get('sector_id'),
            'unitId': form_data.get('unit_id'),
            'costCenterId': form_data.get('cost_center_id'),
            'count': int(form_data.get('count', 0)),
        }
        
        notes = form_data.get('notes')
        if notes:
            data_to_save['notes'] = notes
        elif metric_id:
            data_to_save['notes'] = firestore.DELETE_FIELD

        if metric_id:
            update_document('ticketMetrics', metric_id, data_to_save)
            flash('Métrica atualizada com sucesso!', 'success')
        else:
            add_document('ticketMetrics', data_to_save)
            flash('Métrica registada com sucesso!', 'success')

    except Exception as e:
        current_app.logger.error(f"Erro ao salvar métrica: {e}", exc_info=True)
        flash(f'Ocorreu um erro inesperado ao salvar: {e}', 'danger')
    
    return redirect(url_for('ticket_metrics.list_metrics'))


@ticket_metrics_bp.route('/delete/<string:metric_id>', methods=['POST'])
@login_required
@role_required('admin')
def delete_metric(metric_id: str) -> WerkzeugResponse:
    """Exclui um registo de métrica."""
    try:
        delete_document('ticketMetrics', metric_id)
        flash('Registo de métrica excluído com sucesso!', 'success')
    except Exception as e:
        current_app.logger.error(f"Erro ao excluir métrica {metric_id}: {e}", exc_info=True)
        flash(f'Erro ao excluir registo: {e}', 'danger')
    return redirect(url_for('ticket_metrics.list_metrics'))


# --- Rotas de Importação e Exportação ---

@ticket_metrics_bp.route('/export/csv')
@login_required
@role_required('admin', 'viewer')
def export_metrics_csv() -> Response | WerkzeugResponse:
    """Exporta todas as métricas para um ficheiro CSV."""
    try:
        all_metrics = get_all_documents('ticketMetrics')
        if not all_metrics:
            flash("Não há métricas para exportar.", "info")
            return redirect(url_for('ticket_metrics.list_metrics'))

        context = _get_form_context()
        sectors_map = {s['id']: s.get('name', '') for s in context['sectors']}
        units_map = {u['id']: u.get('name', '') for u in context['units']}
        cost_centers_map = {cc['id']: cc.get('name', '') for cc in context['cost_centers']}
        
        output = io.StringIO()
        writer = csv.writer(output, delimiter=';', lineterminator='\n')
        headers = ['Ano', 'Mes', 'Contagem', 'Setor', 'Unidade', 'Centro de Custo', 'Observacoes']
        writer.writerow(headers)

        for metric in sorted(all_metrics, key=lambda m: (m.get('referenceYear'), m.get('referenceMonth'))):
            row = [
                metric.get('referenceYear', ''), metric.get('referenceMonth', ''),
                metric.get('count', ''), sectors_map.get(metric.get('sectorId'), ''),
                units_map.get(metric.get('unitId'), ''), cost_centers_map.get(metric.get('costCenterId'), ''),
                metric.get('notes', '')
            ]
            writer.writerow(row)

        output.seek(0)
        return Response(output.getvalue(), mimetype="text/csv", headers={"Content-Disposition": "attachment;filename=export_metricas_chamados.csv"})
    except Exception as e:
        current_app.logger.error(f"Erro ao exportar métricas para CSV: {e}", exc_info=True)
        flash("Ocorreu um erro ao gerar o ficheiro de exportação.", "danger")
        return redirect(url_for('ticket_metrics.list_metrics'))


@ticket_metrics_bp.route('/import', methods=['GET', 'POST'])
@login_required
@role_required('admin')
def import_metrics_csv() -> str | WerkzeugResponse:
    """Exibe o formulário de importação (GET) e processa o upload do CSV (POST)."""
    if request.method == 'POST':
        if 'csv_file' not in request.files or not request.files['csv_file'].filename:
            flash('Nenhum ficheiro selecionado.', 'danger')
            return redirect(request.url)
        
        file = request.files['csv_file']
        if not file.filename.endswith('.csv'):
            flash('Formato de ficheiro inválido. Por favor, envie um ficheiro .csv.', 'danger')
            return redirect(request.url)

        try:
            # Cria mapas inversos (Nome -> ID) para validação
            context = _get_form_context()
            sectors_map = {s.get('name'): s['id'] for s in context['sectors']}
            units_map = {u.get('name'): u['id'] for u in context['units']}
            cost_centers_map = {c.get('name'): c['id'] for c in context['cost_centers']}
            
            df = pd.read_csv(file.stream, sep=';', encoding='utf-8', keep_default_na=False, dtype=str)
            success_count, error_count, errors = 0, 0, []

            for index, row in df.iterrows():
                try:
                    required_cols = ['Ano', 'Mes', 'Contagem', 'Setor', 'Unidade', 'Centro de Custo']
                    if not all(col in row and str(row[col]).strip() for col in required_cols):
                        raise ValueError("Colunas obrigatórias em falta ou vazias.")

                    sector_id = sectors_map.get(row['Setor'])
                    if not sector_id: raise ValueError(f"Setor '{row['Setor']}' não encontrado.")
                    
                    unit_id = units_map.get(row['Unidade'])
                    if not unit_id: raise ValueError(f"Unidade '{row['Unidade']}' não encontrada.")
                    
                    cc_id = cost_centers_map.get(row['Centro de Custo'])
                    if not cc_id: raise ValueError(f"Centro de Custo '{row['Centro de Custo']}' não encontrado.")

                    data_to_save = {
                        'referenceYear': int(row['Ano']), 'referenceMonth': int(row['Mes']),
                        'count': int(row['Contagem']), 'sectorId': sector_id,
                        'unitId': unit_id, 'costCenterId': cc_id,
                        'notes': row.get('Observacoes', '')
                    }
                    add_document('ticketMetrics', data_to_save)
                    success_count += 1
                except Exception as row_error:
                    error_count += 1
                    errors.append(f"Linha {index + 2}: {row_error}")
            
            if success_count > 0: flash(f'{success_count} registos importados com sucesso!', 'success')
            if error_count > 0:
                flash(f'{error_count} linhas foram ignoradas devido a erros.', 'danger')
                for err in errors[:5]: flash(err, 'danger') # Mostra os primeiros 5 erros
            
            return redirect(url_for('ticket_metrics.list_metrics'))
        except Exception as e:
            current_app.logger.error(f"Erro ao processar o ficheiro CSV: {e}", exc_info=True)
            flash(f"Ocorreu um erro ao ler o ficheiro: {e}", 'danger')
            return redirect(request.url)
            
    return render_template('ticket_metrics/import_form.html')


@ticket_metrics_bp.route('/export/template/csv')
@login_required
@role_required('admin')
def download_metric_template_csv() -> Response:
    """Fornece o template CSV para download, alinhado com o novo modelo de dados."""
    output = io.StringIO()
    writer = csv.writer(output, delimiter=';', lineterminator='\n')
    headers = ['Ano', 'Mes', 'Contagem', 'Setor', 'Unidade', 'Centro de Custo', 'Observacoes']
    writer.writerow(headers)
    writer.writerow(['2025', '6', '15', 'Tecnologia da Informação', 'Unidade Matriz', 'Centro de Custo TI', 'Observação de exemplo'])
    output.seek(0)
    return Response(output.getvalue(), mimetype="text/csv", headers={"Content-Disposition": "attachment;filename=template_importacao_metricas.csv"})