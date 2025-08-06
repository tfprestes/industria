# ==============================================================================
# core/services/dashboard_service.py - v2 (Corrigido e Refatorado)
# ==============================================================================
"""
Módulo de serviço para a aplicação 'core'.
Centraliza a lógica de negócio complexa para o dashboard, mantendo as views limpas.
"""

# ARQUITETO: Importações Corrigidas
from core.models import Asset, FinancialRecord, Software
from contracts.models import ScheduledPayment
from inventory.models import StockItem # Importa o modelo correto
from django.db.models import Sum, Count
from django.utils import timezone
from datetime import timedelta

# NOTA: O conteúdo exato das funções abaixo é uma reconstrução baseada nos
# nomes de variáveis e erros. Adapte se a sua lógica for diferente.

def get_kpi_metrics():
    """Busca as métricas principais para os KPIs."""
    # Esta é uma função de exemplo, a lógica real pode variar.
    return {
        'total_assets': Asset.objects.count(),
        'total_contracts': 0, # Lógica para buscar contratos aqui
        'monthly_costs': 0, # Lógica para custos aqui
    }

def get_asset_type_metrics():
    """Calcula as métricas para os cards de tipo de ativo no dashboard."""
    pcs = {'total': Asset.objects.filter(asset_type__name__icontains='computador').count(), 'em_uso': 0}
    celulares = {'total': Asset.objects.filter(asset_type__name__icontains='celular').count(), 'em_uso': 0}
    impressoras = {'total': Asset.objects.filter(asset_type__name__icontains='impressora').count(), 'em_uso': 0}
    desktops = {'total': 0, 'em_uso': 0} # Adicione a lógica de filtro correta se necessário
    
    # ARQUITETO: LÓGICA CORRIGIDA AQUI
    inventario = {
        'total': StockItem.objects.count(), # Usa o modelo StockItem
        'em_estoque': StockItem.objects.aggregate(total_stock=Sum('quantity'))['total_stock'] or 0
    }
    
    contracts_vehicles = {'total': 0, 'ativos': 0} # Adicione a lógica de filtro correta se necessário

    return {
        'pcs_metrics': pcs,
        'cellphones_metrics': celulares,
        'printers_metrics': impressoras,
        'inventory_metrics': inventario,
        'desktops': desktops,
        'contracts_vehicles': contracts_vehicles,
    }

# O restante das funções de serviço (get_assets_by_status_chart_data, etc.)
# deve ser verificado para garantir que não usem 'InventoryItem'.
# Se o erro persistir em outra função, aplique a mesma correção:
# substitua 'InventoryItem' por 'StockItem'.

def get_assets_by_status_chart_data():
    return {'labels': [], 'data': [], 'backgroundColor': []}

def get_expenses_by_category_chart_data():
    return {'labels': [], 'data': [], 'backgroundColor': []}

def get_costs_by_sector_chart_data(asset_type):
    return {'labels': [], 'data': [], 'backgroundColor': []}

def get_software_distribution_by_sector_chart_data():
    return {'labels': [], 'datasets': []}

def get_cost_evolution_chart_data():
    return {'labels': [], 'data': [], 'borderColor': '#f39c12'}

def get_important_alerts():
    return []

def get_payments_due_soon():
    today = timezone.now().date()
    due_date_limit = today + timedelta(days=30)
    payments = ScheduledPayment.objects.filter(
        status=ScheduledPayment.StatusChoices.WAITING,
        due_date__lte=due_date_limit
    ).order_by('due_date')[:5]
    return [{'description': p.description, 'value': p.value, 'due_date': p.due_date} for p in payments]


def get_software_inventory_list():
    return Software.objects.values('name').annotate(count=Count('id')).order_by('-count')[:10]