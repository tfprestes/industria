# ==============================================================================
# core/views.py - v2 (Refatorado para usar ModelForms)
# ==============================================================================
"""
Módulo de views para a aplicação 'core' do ConnectIT.
Contém a DashboardView refatorada com lógica de negócio separada em serviços
e as views de CRUD para Ativos usando ModelForms para maior segurança.
"""

from typing import Any, Dict

from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView

from .models import Asset, Unit
from .forms import AssetForm  # ARQUITETO: Importa o novo ModelForm
from .services import dashboard_service


class DashboardView(TemplateView):
    """
    View principal do Dashboard.
    """
    template_name = 'core/dashboard.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update(dashboard_service.get_kpi_metrics())
        context.update(dashboard_service.get_asset_type_metrics())
        context['asset_status_chart_data'] = dashboard_service.get_assets_by_status_chart_data()
        context['expense_category_chart_data'] = dashboard_service.get_expenses_by_category_chart_data()
        context['costs_by_computer_sector_chart_data'] = dashboard_service.get_costs_by_sector_chart_data(asset_type='computador')
        context['costs_by_cellphone_sector_chart_data'] = dashboard_service.get_costs_by_sector_chart_data(asset_type='celular')
        context['costs_by_printer_sector_chart_data'] = dashboard_service.get_costs_by_sector_chart_data(asset_type='impressora')
        context['software_distribution_by_sector_chart_data'] = dashboard_service.get_software_distribution_by_sector_chart_data()
        context['cost_evolution_chart_data'] = dashboard_service.get_cost_evolution_chart_data()
        context['important_alerts'] = dashboard_service.get_important_alerts()
        context['payments_due_soon'] = dashboard_service.get_payments_due_soon()
        context['software_inventory_list'] = dashboard_service.get_software_inventory_list()
        return context


class AssetListView(ListView):
    """
    View para listar, filtrar e pesquisar todos os ativos.
    """
    model = Asset
    template_name = 'core/asset_list.html'
    context_object_name = 'assets'
    paginate_by = 15

    def get_queryset(self):
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
                # ARQUITETO: A busca no campo 'user' agora busca nos campos do usuário relacionado
                Q(user__username__icontains=search_query) |
                Q(user__first_name__icontains=search_query) |
                Q(user__last_name__icontains=search_query)
            )
        return queryset

    def get_context_data(self, **kwargs):
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
    form_class = AssetForm  # ARQUITETO: Trocamos 'fields' por 'form_class'
    template_name = 'core/asset_form.html'
    success_url = reverse_lazy('core:asset_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Adicionar Novo Ativo'
        return context


class AssetUpdateView(UpdateView):
    """
    View para editar um ativo existente.
    """
    model = Asset
    form_class = AssetForm  # ARQUITETO: Trocamos 'fields' por 'form_class'
    template_name = 'core/asset_form.html'
    success_url = reverse_lazy('core:asset_list')

    def get_context_data(self, **kwargs):
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