# app/routes/dashboard_routes.py (Versão Final com Layout Otimizado)

import datetime
from typing import Any, Dict
import pandas as pd
from dateutil.relativedelta import relativedelta
from flask import Blueprint, Response, current_app, jsonify, render_template, request
from app.auth.routes import login_required
from app.services.firestore_service import (get_all_documents,
                                            get_collection_size,
                                            get_documents_with_query)

dashboard_bp = Blueprint('dashboard', __name__, url_prefix='/')

@dashboard_bp.route('/')
@login_required
def index() -> str:
    """Renderiza a página principal do dashboard."""
    return render_template('dashboard/index.html')

@dashboard_bp.route('/api/dashboard/kpi_cards')
@login_required
def get_kpi_cards_data() -> Response:
    # Esta função está correta e permanece a mesma.
    try:
        assets_docs = get_all_documents('assets')
        inventory_docs = get_all_documents('inventory')
        asset_types_map = {at['id']: at.get('name', 'N/A').lower() for at in get_all_documents('assetTypes')}
        today = datetime.datetime.now(datetime.timezone.utc)
        ninety_days_from_now = today + relativedelta(days=90)
        expiring_contracts_query = [{'field': 'endDate', 'op': '>=', 'value': today}, {'field': 'endDate', 'op': '<=', 'value': ninety_days_from_now}]
        expiring_contracts_count = len(get_documents_with_query('contracts', expiring_contracts_query))
        df_assets = pd.DataFrame(assets_docs) if assets_docs else pd.DataFrame()
        asset_counts = {}
        if not df_assets.empty and 'assetTypeId' in df_assets.columns:
            df_assets['assetTypeName'] = df_assets['assetTypeId'].map(asset_types_map).fillna('desconhecido')
            asset_counts = df_assets['assetTypeName'].value_counts().to_dict()
        kpi_data = {
            'count_computers': asset_counts.get('computador', 0) + asset_counts.get('notebook', 0),
            'count_mobiles': asset_counts.get('celular', 0),
            'count_printers': asset_counts.get('impressora', 0),
            'total_network_equipment': get_collection_size('networkEquipment'),
            'total_inventory_items': sum(item.get('quantity', 0) for item in inventory_docs),
            'expiring_contracts_count': expiring_contracts_count,
            'count_nobreaks': asset_counts.get('nobreak', 0),
            'count_wifi_points': asset_counts.get('wifi', 0) + asset_counts.get('unifi', 0),
            'count_cameras': asset_counts.get('camera', 0) + asset_counts.get('câmera', 0),
            'count_access_controllers': asset_counts.get('controlador de acesso', 0),
            'count_extensions': get_collection_size('extensions')
        }
        return jsonify(kpi_data)
    except Exception as e:
        current_app.logger.error(f"Erro na API de KPIs: {e}", exc_info=True)
        return jsonify({'error': 'Falha ao processar dados dos KPIs'}), 500


@dashboard_bp.route('/api/dashboard/alerts')
@login_required
def get_alerts_data() -> Response:
    """Retorna os dados para o painel de Alertas Importantes."""
    try:
        today = datetime.datetime.now(datetime.timezone.utc)
        today_date = today.date()
        alert_horizon = today_date + datetime.timedelta(days=7)

        expiring_contracts_query = [{'field': 'endDate', 'op': '>=', 'value': today}, {'field': 'endDate', 'op': '<=', 'value': today + relativedelta(days=90)}]
        expiring_contracts = get_documents_with_query('contracts', expiring_contracts_query, limit=3, order_by='endDate')
        
        low_stock_items_docs = get_all_documents('inventory')
        low_stock_items = [item for item in low_stock_items_docs if item.get('minStockLevel', 0) > 0 and item.get('quantity', 0) <= item.get('minStockLevel', 0)][:3]

        upcoming_payments = []
        active_monthly_contracts_query = [{'field': 'status', 'op': '==', 'value': 'Ativo'}, {'field': 'billingCycle', 'op': '==', 'value': 'Mensal'}]
        active_contracts = get_documents_with_query('contracts', active_monthly_contracts_query)

        for contract in active_contracts:
            payment_day = contract.get('paymentDay')
            if isinstance(payment_day, int) and 1 <= payment_day <= 31:
                # Reutilizando a lógica de cálculo de data de vencimento que definimos
                next_due_date = _calculate_next_due_date(payment_day, today_date)
                if today_date <= next_due_date <= alert_horizon:
                    upcoming_payments.append({'id': contract.get('id'), 'name': contract.get('name', 'N/A'), 'value': contract.get('value', 0), 'dueDateFormatted': next_due_date.strftime('%d/%m/%Y')})
        
        upcoming_payments.sort(key=lambda p: datetime.datetime.strptime(p['dueDateFormatted'], '%d/%m/%Y'))

        expiring_contracts_data = [{'id': asset.get('id'), 'name': asset.get('name', 'N/A'), 'endDate': asset.get('endDate').strftime('%d/%m/%Y')} for asset in expiring_contracts]
        low_stock_data = [{'id': item.get('id'), 'name': item.get('itemName', 'N/A'), 'quantity': item.get('quantity', 0), 'minStock': item.get('minStockLevel', 0)} for item in low_stock_items]

        return jsonify({'expiring_contracts': expiring_contracts_data, 'low_stock_items': low_stock_data, 'upcoming_payments': upcoming_payments[:3]})
    except Exception as e:
        current_app.logger.error(f"Erro na API de Alertas: {e}", exc_info=True)
        return jsonify({'error': 'Falha ao processar dados de Alertas'}), 500


@dashboard_bp.route('/api/dashboard/asset_costs_by_sector')
@login_required
def get_asset_costs_by_sector() -> Response:
    # Esta função está correta e permanece a mesma.
    try:
        target_asset_type = request.args.get('type', default=None, type=str)
        if not target_asset_type: return jsonify({'error': 'O tipo de ativo é obrigatório'}), 400
        asset_types = get_all_documents('assetTypes')
        asset_types_map_name_to_id = {at.get('name', 'N/A').lower(): at['id'] for at in asset_types}
        target_asset_type_id = asset_types_map_name_to_id.get(target_asset_type.lower())
        if not target_asset_type_id: return jsonify({'labels': [], 'data': []})
        assets_docs = get_documents_with_query('assets', [{'field': 'assetTypeId', 'op': '==', 'value': target_asset_type_id}])
        if not assets_docs: return jsonify({'labels': [], 'data': []})
        sectors_map = {s['id']: s.get('name', 'Não Classificado') for s in get_all_documents('sectors')}
        df = pd.DataFrame(assets_docs)
        df['leaseValue'] = pd.to_numeric(df['leaseValue'], errors='coerce').fillna(0)
        df['sectorName'] = df['assignedSectorId'].map(sectors_map).fillna('Não Classificado')
        costs_by_sector = df.groupby('sectorName')['leaseValue'].sum().round(2).sort_values(ascending=True)
        return jsonify({'labels': costs_by_sector.index.tolist(), 'data': costs_by_sector.values.tolist()})
    except Exception as e:
        current_app.logger.error(f"Erro na API de custos por setor para '{target_asset_type}': {e}", exc_info=True)
        return jsonify({'error': f"Falha ao processar dados para '{target_asset_type}'"}), 500

@dashboard_bp.route('/api/dashboard/software_by_sector')
@login_required
def api_software_by_sector() -> Response:
    """Endpoint que retorna a distribuição de Office e SO por setor."""
    # (código mantido e validado)
    try:
        assets_docs = get_all_documents('assets')
        if not assets_docs: return jsonify({'labels': [], 'datasets': []})
        sectors_map = {s['id']: s.get('name', 'Não Classificado') for s in get_all_documents('sectors')}
        df = pd.DataFrame(assets_docs)
        df = df.dropna(subset=['assignedSectorId'])
        df['sectorName'] = df['assignedSectorId'].map(sectors_map).fillna('Não Classificado')
        df_os = df[['sectorName', 'operatingSystem']].rename(columns={'operatingSystem': 'software'}).dropna()
        df_os = df_os[df_os['software'] != '']
        df_office = df[['sectorName', 'officeVersion']].rename(columns={'officeVersion': 'software'}).dropna()
        df_office = df_office[df_office['software'] != '']
        df_combined = pd.concat([df_os, df_office])
        cross_tab = pd.crosstab(df_combined['sectorName'], df_combined['software'])
        relevant_software = [s for s in ['Windows 11 Pro', 'Windows 10 Pro', 'Office 365', 'Office 2019 Standard'] if s in cross_tab.columns]
        if not relevant_software: return jsonify({'labels': [], 'datasets': []})
        cross_tab = cross_tab[relevant_software]
        top_sectors = cross_tab.sum(axis=1).nlargest(7).index
        cross_tab = cross_tab.loc[top_sectors]
        datasets = []
        colors = ['#3b82f6', '#14b8a6', '#ef4444', '#f59e0b', '#8b5cf6']
        for i, column in enumerate(cross_tab.columns):
            datasets.append({'label': column, 'data': cross_tab[column].tolist(), 'backgroundColor': colors[i % len(colors)]})
        return jsonify({'labels': cross_tab.index.tolist(), 'datasets': datasets})
    except Exception as e:
        current_app.logger.error(f"Erro na API de software por setor: {e}", exc_info=True)
        return jsonify({'error': 'Falha ao processar dados de software por setor'}), 500

@dashboard_bp.route('/api/dashboard/software_inventory')
@login_required
def get_software_inventory() -> Response:
    """Retorna a contagem de versões do Windows e Office para o painel lateral."""
    # (código mantido e validado)
    try:
        assets_docs = get_all_documents('assets')
        if not assets_docs: return jsonify({'windows_counts': [], 'office_counts': []})
        df = pd.DataFrame(assets_docs)
        df_win = df.dropna(subset=['operatingSystem'])
        df_off = df.dropna(subset=['officeVersion'])
        windows_counts = df_win[df_win['operatingSystem'].str.contains('Windows', na=False, case=False)]['operatingSystem'].str.strip().value_counts()
        office_counts = df_off[df_off['officeVersion'].str.contains('Office', na=False, case=False)]['officeVersion'].str.strip().value_counts()
        return jsonify({'windows_counts': [{'name': k, 'count': v} for k, v in windows_counts.items()][:3], 'office_counts': [{'name': k, 'count': v} for k, v in office_counts.items()][:3]})
    except Exception as e:
        current_app.logger.error(f"Erro na API de inventário de software: {e}", exc_info=True)
        return jsonify({'error': 'Falha ao processar os dados de software'}), 500


@dashboard_bp.route('/api/dashboard/maintenance_evolution')
@login_required
def get_maintenance_evolution() -> Response:
    """Retorna os custos de manutenção dos últimos 12 meses."""
    # (código mantido e validado)
    try:
        twelve_months_ago = datetime.datetime.now(datetime.timezone.utc) - relativedelta(months=12)
        maintenance_logs = get_documents_with_query('maintenanceLogs', [{'field': 'logDate', 'op': '>=', 'value': twelve_months_ago}])
        if not maintenance_logs: return jsonify({'labels': [], 'datasets': []})
        df = pd.DataFrame(maintenance_logs)
        df['logDate'] = pd.to_datetime(df['logDate'], errors='coerce')
        df = df.dropna(subset=['logDate'])
        df['month_year'] = df['logDate'].dt.to_period('M')
        df['cost'] = pd.to_numeric(df['cost'], errors='coerce').fillna(0)
        maint_by_month = df.groupby('month_year')['cost'].sum().sort_index()
        today = datetime.date.today()
        last_12_months = pd.period_range(start=today - relativedelta(months=11), end=today, freq='M')
        maint_by_month = maint_by_month.reindex(last_12_months, fill_value=0)
        return jsonify({'labels': [p.strftime('%b/%y') for p in maint_by_month.index], 'datasets': [{'label': 'Custo de Manutenção (R$)', 'data': maint_by_month.values.tolist(), 'borderColor': '#f59e0b', 'tension': 0.3}]})
    except Exception as e:
        current_app.logger.error(f"Erro na API de evolução de manutenção: {e}", exc_info=True)
        return jsonify({'error': 'Falha ao processar dados de manutenção'}), 500

# Adicionando a função auxiliar para cálculo de data
def _calculate_next_due_date(payment_day: int, today: datetime.date) -> datetime.date:
    """
    Calcula a próxima data de vencimento para um dia de pagamento mensal.
    """
    try:
        next_due = today.replace(day=payment_day)
    except ValueError:
        next_month_first_day = today.replace(day=1) + relativedelta(months=1)
        next_due = next_month_first_day - datetime.timedelta(days=1)

    if today > next_due:
        try:
            next_due = (today + relativedelta(months=1)).replace(day=payment_day)
        except ValueError:
            next_two_months_first_day = today.replace(day=1) + relativedelta(months=2)
            next_due = next_two_months_first_day - datetime.timedelta(days=1)
    return next_due