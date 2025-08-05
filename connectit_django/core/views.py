# ==============================================================================
# connectit_django/core/views.py - Refatorado e Corrigido como Arquiteto de Software Sênior
# ==============================================================================
"""
Módulo de views para a aplicação 'core' do ConnectIT.
Contém a DashboardView refatorada com lógica de negócio separada em serviços
e as views de CRUD para Ativos.
"""

from typing import Any, Dict

from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView

from core.models import Asset, Unit
from core.services import dashboard_service


class DashboardView(TemplateView):
    """
    View principal do Dashboard.
    Coleta dados de diversas fontes através de uma camada de serviço
    e os prepara para exibição no template.
    """
    template_name = 'core/dashboard.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        """
        Popula o contexto do template com todos os dados necessários para o dashboard.
        Os dados são obtidos através de funções na camada de serviço para manter
        a view limpa e focada na apresentação.
        """
        context = super().get_context_data(**kwargs)

        # --- DADOS PARA OS CARTÕES DE KPI (Key Performance Indicators) ---
        context.update(dashboard_service.get_kpi_metrics())

        # --- DADOS DETALHADOS POR TIPO DE ATIVO PARA OS CARDS SUPERIORES ---
        context.update(dashboard_service.get_asset_type_metrics())

        # --- DADOS PARA OS GRÁFICOS ---
        # Gráfico 1: Ativos por Status (Doughnut Chart)
        context['asset_status_chart_data'] = dashboard_service.get_assets_by_status_chart_data()

        # Gráfico 2: Despesas por Categoria (Bar Chart)
        context['expense_category_chart_data'] = dashboard_service.get_expenses_by_category_chart_data()

        # Gráficos 3, 4, 5: Custos por Setor (Barras Horizontais)
        context['costs_by_computer_sector_chart_data'] = dashboard_service.get_costs_by_sector_chart_data(asset_type='computador')
        context['costs_by_cellphone_sector_chart_data'] = dashboard_service.get_costs_by_sector_chart_data(asset_type='celular')
        context['costs_by_printer_sector_chart_data'] = dashboard_service.get_costs_by_sector_chart_data(asset_type='impressora')

        # Gráfico 6: Distribuição de Software por Setor (Barras Empilhadas)
        context['software_distribution_by_sector_chart_data'] = dashboard_service.get_software_distribution_by_sector_chart_data()

        # Gráfico 7: Evolução de Custos (Linha)
        context['cost_evolution_chart_data'] = dashboard_service.get_cost_evolution_chart_data()

        # --- DADOS PARA AS TABELAS/LISTAS INFERIORES ---
        # Tabela 1: Alertas Importantes (ex.: ativos com status de alerta ou contratos críticos)
        context['important_alerts'] = dashboard_service.get_important_alerts()

        # Tabela 2: Pagamentos a Vencer
        context['payments_due_soon'] = dashboard_service.get_payments_due_soon()

        # Tabela 3: Inventário de Software
        context['software_inventory_list'] = dashboard_service.get_software_inventory_list()

        # As variáveis acima serão convertidas em JSON no template com o filtro |json_script

        return context


# ==============================================================================
# CRUD VIEWS DE ATIVOS
# ==============================================================================

class AssetListView(ListView):
    """
    View para listar, filtrar e pesquisar todos os ativos.
    """
    model = Asset
    template_name = 'core/asset_list.html'
    context_object_name = 'assets'
    paginate_by = 15

    def get_queryset(self):
        """
        Sobrescreve o método padrão para adicionar lógica de filtro e pesquisa.
        """
        queryset = super().get_queryset().select_related(
            'asset_type', 'assigned_unit', 'assigned_sector', 'responsible'
        )

        status_filter = self.request.GET.get('status', '')
        unit_filter = self.request.GET.get('unit', '')
        search_query = self.request.GET.get('search', '')

        if status_filter:
            queryset = queryset.filter(status=status_filter)

        if unit_filter:
            queryset = queryset.filter(assigned_unit_id=unit_filter)

        if search_query:
            queryset = queryset.filter(
                Q(internal_tag__icontains=search_query) |
                Q(serial_number__icontains=search_query) |
                Q(brand__icontains=search_query) |
                Q(model__icontains=search_query) |
                Q(user__icontains=search_query)
            )

        return queryset

    def get_context_data(self, **kwargs):
        """
        Adiciona dados extras ao contexto para os filtros e a pesquisa do template.
        """
        context = super().get_context_data(**kwargs)
        context['all_units'] = Unit.objects.all()
        context['status_choices'] = Asset.StatusChoices.choices
        context['current_status'] = self.request.GET.get('status', '')
        context['current_unit'] = self.request.GET.get('unit', '')
        context['search_query'] = self.request.GET.get('search', '')
        return context


class AssetCreateView(CreateView):
    """
    View para criar um novo ativo.
    """
    model = Asset
    template_name = 'core/asset_form.html'
    fields = '__all__'
    success_url = reverse_lazy('core:asset_list')

    def get_context_data(self, **kwargs):
        """Adiciona um título dinâmico à página."""
        context = super().get_context_data(**kwargs)
        context['title'] = 'Adicionar Novo Ativo'
        return context


class AssetUpdateView(UpdateView):
    """
    View para editar um ativo existente.
    """
    model = Asset
    template_name = 'core/asset_form.html'
    fields = '__all__'
    success_url = reverse_lazy('core:asset_list')

    def get_context_data(self, **kwargs):
        """Adiciona um título dinâmico à página."""
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Ativo'
        return context


class AssetDeleteView(DeleteView):
    """
    View para excluir um ativo, com uma página de confirmação.
    """
    model = Asset
    template_name = 'core/asset_confirm_delete.html'
    success_url = reverse_lazy('core:asset_list')
    context_object_name = 'asset'
