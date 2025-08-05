# ==============================================================================
# connectit_app/core/services/dashboard_service.py - Nova Camada de Serviço
# ==============================================================================
"""
Módulo de serviço para o Dashboard.
Contém a lógica de negócio e as consultas ao banco de dados para
preparar os dados exibidos no dashboard, seguindo o SRP.
"""

from datetime import date, timedelta
from typing import Dict, List, Any, Union
from django.db.models import Count, Sum, Q, F
from django.db.models.functions import TruncMonth

# --- Importações dos Modelos (AJUSTADO CONFORME AS PREMISSAS MAIS PROVÁVEIS) ---
# VERIFIQUE E AJUSTE ESTAS IMPORTAÇÕES COM SEUS MODELOS REAIS PARA EVITAR 'ImportError'!
# PREMISSA: Modelos sem apps dedicadas (software, finance, ou inventory.models não funcional)
#           são assumidos como estando em 'core.models'.

from core.models import Asset, Unit, Sector, InventoryItem, Software, SoftwareCategory, FinancialRecord
# Modelos abaixo são assumidos como estando em seus próprios apps
from contracts.models import ScheduledPayment, Contract
from expenses.models import Expense

def get_kpi_metrics() -> Dict[str, Union[int, float]]:
    """
    Retorna as métricas de KPI gerais para os cards do dashboard.
    """
    total_assets = Asset.objects.count()
    active_contracts = Contract.objects.filter(status=Contract.StatusChoices.ACTIVE).count()
    pending_payments = ScheduledPayment.objects.filter(status=Contract.StatusChoices.WAITING).count()

    # Custo mensal previsto somando o valor dos contratos ativos
    projected_cost_agg = Contract.objects.filter(status=Contract.StatusChoices.ACTIVE).aggregate(total=Sum('monthly_value'))
    projected_monthly_cost = projected_cost_agg['total'] or 0.00

    return {
        'total_assets': total_assets,
        'active_contracts': active_contracts,
        'pending_payments': pending_payments,
        'projected_monthly_cost': projected_monthly_cost,
    }

def get_asset_type_metrics() -> Dict[str, Dict[str, int]]:
    """
    Retorna as métricas detalhadas por tipo de ativo para os cards superiores
    (Computadores, Celulares, Impressoras, Desktops, Itens Inventário, Contratos e Veículos).
    Os nomes das chaves no dicionário devem corresponder exatamente aos nomes
    esperados no template.
    """
    metrics: Dict[str, Dict[str, int]] = {}

    # Exemplo: Computadores
    # Assumindo que 'asset_type' é um campo de ForeignKey em Asset para um modelo com campo 'name'
    # E que 'status' é um campo em Asset (ex: 'ativo', 'em_manutencao', etc.)
    metrics['computadores'] = {
        'total': Asset.objects.filter(asset_type__name='Computador').count(), 
        'em_uso': Asset.objects.filter(asset_type__name='Computador', status='ativo').count(), 
    }

    metrics['celulares'] = {
        'total': Asset.objects.filter(asset_type__name='Celular').count(),
        'em_uso': Asset.objects.filter(asset_type__name='Celular', status='ativo').count(),
    }

    metrics['impressoras'] = {
        'total': Asset.objects.filter(asset_type__name='Impressora').count(),
        'em_uso': Asset.objects.filter(asset_type__name='Impressora', status='ativo').count(),
    }
    
    metrics['desktops'] = {
        'total': Asset.objects.filter(asset_type__name='Desktop').count(),
        'em_uso': Asset.objects.filter(asset_type__name='Desktop', status='ativo').count(),
    }
    
    metrics['inventory_items'] = {
        'total': InventoryItem.objects.count(), 
        'em_estoque': InventoryItem.objects.filter(status='em_estoque').count(), 
    }

    metrics['contracts_vehicles'] = {
        'total': Contract.objects.count(),
        'ativos': Contract.objects.filter(status=Contract.StatusChoices.ACTIVE).count(),
    }

    return metrics


def get_assets_by_status_chart_data() -> Dict[str, List[Any]]:
    """
    Retorna os dados para o gráfico de pizza/doughnut de Ativos por Status.
    """
    assets_by_status = Asset.objects.values('status').annotate(count=Count('id')).order_by('status')
    return {
        'labels': [dict(Asset.StatusChoices.choices).get(item['status'], item['status']) for item in assets_by_status],
        'data': [item['count'] for item in assets_by_status],
        'backgroundColor': ['#3498db', '#e74c3c', '#2ecc71', '#f39c12', '#9b59b6']
    }

def get_expenses_by_category_chart_data() -> Dict[str, List[Any]]:
    """
    Retorna os dados para o gráfico de barras de Despesas por Categoria.
    """
    expenses_by_category = (
        Expense.objects.values('expense_type__name')
        .annotate(total=Sum('value'))
        .order_by('-total')
    )
    return {
        'labels': [item['expense_type__name'] for item in expenses_by_category],
        'data': [float(item['total']) for item in expenses_by_category],
        'backgroundColor': '#2ecc71', 
    }

def get_costs_by_sector_chart_data(asset_type: str) -> Dict[str, List[Any]]:
    """
    Retorna os dados para os gráficos de Custo por Setor para um tipo de ativo específico.
    Assume que Asset tem um campo 'assigned_sector' (ForeignKey para Sector) e 'cost' (DecimalField).
    """
    costs_data = (
        Asset.objects.filter(asset_type__name__iexact=asset_type) 
        .values('assigned_sector__name') 
        .annotate(total_cost=Sum('cost')) 
        .order_by('-total_cost') 
    )
    
    labels = [item['assigned_sector__name'] or 'Não Atribuído' for item in costs_data]
    data = [float(item['total_cost'] or 0.0) for item in costs_data]

    colors = {
        'computador': 'rgba(66, 135, 245, 0.8)', 
        'celular': 'rgba(40, 167, 69, 0.8)', 
        'impressora': 'rgba(255, 193, 7, 0.8)', 
        'desktop': 'rgba(108, 117, 125, 0.8)', 
    }

    return {
        "labels": labels,
        "data": data,
        "backgroundColor": colors.get(asset_type, 'rgba(140, 140, 140, 0.8)')
    }

def get_software_distribution_by_sector_chart_data() -> Dict[str, Any]:
    """
    Retorna os dados para o gráfico de barras empilhadas de Distribuição de Software por Setor.
    Assume que Software tem um ForeignKey para Asset (ou Sector direto) e um campo 'category'.
    """
    sectors = Sector.objects.all().order_by('name')
    sector_names = [s.name for s in sectors]

    software_categories = SoftwareCategory.objects.all().order_by('name')
    category_names = [sc.name for sc in software_categories]

    datasets: List[Dict[str, Any]] = []
    colors_map = {
        'Produtividade': 'rgba(75, 192, 192, 0.8)',
        'Segurança': 'rgba(255, 99, 132, 0.8)',
        'Desenvolvimento': 'rgba(54, 162, 235, 0.8)',
        'Design': 'rgba(255, 205, 86, 0.8)',
        'Sistema Operacional': 'rgba(153, 102, 255, 0.8)',
        'Outros': 'rgba(201, 203, 207, 0.8)'
    }

    for category_name in category_names:
        data_for_category: List[int] = []
        for sector_name in sector_names:
            # Esta consulta é um exemplo e precisa ser adaptada à sua modelagem.
            # Se Software está ligado a Asset (que tem o Setor):
            count = Software.objects.filter(
                category__name=category_name, 
                asset__assigned_sector__name=sector_name 
            ).count()
            data_for_category.append(count)
        
        datasets.append({
            'label': category_name,
            'data': data_for_category,
            'backgroundColor': colors_map.get(category_name, 'rgba(100, 100, 100, 0.8)')
        })

    return {
        'labels': sector_names,
        'datasets': datasets,
    }


def get_cost_evolution_chart_data() -> Dict[str, Any]:
    """
    Retorna os dados para o gráfico de linha de Evolução de Custos ao longo do tempo.
    Assume um modelo FinancialRecord com campos 'date' e 'value' e 'type' ('despesa').
    """
    today = date.today()
    start_date = today - timedelta(days=365) 

    monthly_expenses = FinancialRecord.objects.filter(
        type='despesa', 
        date__gte=start_date
    ).annotate(
        month=TruncMonth('date')
    ).values('month').annotate(
        total_value=Sum('value')
    ).order_by('month')

    labels: List[str] = []
    data: List[float] = []

    for entry in monthly_expenses:
        labels.append(entry['month'].strftime('%b/%Y')) 
        data.append(float(entry['total_value'] or 0.0))

    return {
        'labels': labels,
        'data': data,
        'borderColor': '#f39c12', 
        'tension': 0.4, 
    }

def get_important_alerts() -> List[Dict[str, str]]:
    """
    Retorna uma lista de alertas importantes.
    Exemplo: Ativos com status de alerta, contratos críticos, etc.
    """
    alerts: List[Dict[str, str]] = []
    today = date.today()
    ninety_days_from_now = today + timedelta(days=90)

    # Contratos expirando
    expiring_contracts = Contract.objects.filter(
        status=Contract.StatusChoices.ACTIVE,
        end_date__lte=ninety_days_from_now,
        end_date__gte=today 
    ).order_by('end_date')[:5]

    for contract in expiring_contracts:
        alerts.append({
            'type': 'Contrato',
            'description': f"Contrato com {contract.supplier.name} expira em {contract.end_date.strftime('%d/%m/%Y')}",
            'severity': 'warning' 
        })
    
    # Exemplo: Ativos em manutenção ou com status crítico
    critical_assets = Asset.objects.filter(status='manutencao').select_related('asset_type')[:5]
    for asset in critical_assets:
        alerts.append({
            'type': 'Ativo',
            'description': f"Ativo '{asset.internal_tag}' ({asset.asset_type.name}) em manutenção.",
            'severity': 'info'
        })

    return alerts[:5] 

def get_payments_due_soon() -> List[Dict[str, Any]]:
    """
    Retorna uma lista de pagamentos a vencer em breve.
    """
    today = date.today()
    next_30_days = today + timedelta(days=30) 

    payments = ScheduledPayment.objects.filter(
        status=ScheduledPayment.StatusChoices.WAITING,
        due_date__gte=today,
        due_date__lte=next_30_days
    ).select_related('contract__supplier').order_by('due_date')[:5]

    result: List[Dict[str, Any]] = []
    for p in payments:
        result.append({
            'description': f"Pagamento: {p.description or 'N/A'}", # <-- AQUI ESTÁ A LINHA PROBLEMA
            'supplier': p.contract.supplier.name if p.contract and p.contract.supplier else 'N/A',
            'amount': float(p.value or 0.0), # <-- ALTERADO DE 'amount' PARA 'value'
            'due_date': p.due_date.strftime('%d/%m/%Y')
        })
    return result

def get_software_inventory_list() -> List[Dict[str, Any]]:
    """
    Retorna uma lista resumida do inventário de software.
    """
    software_counts = Software.objects.values('name').annotate(total=Count('id')).order_by('-total')[:5]
    result: List[Dict[str, Any]] = []
    for s_count in software_counts:
        result.append({
            'name': s_count['name'],
            'count': s_count['total']
        })
    return result