# Em: contracts/views.py

from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Contract, ContractType

class ContractListView(ListView):
    model = Contract
    template_name = 'contracts/contract_list.html'
    context_object_name = 'contracts'
    paginate_by = 10

    def get_queryset(self):
        """Adiciona lógica de filtro e pesquisa."""
        queryset = super().get_queryset().select_related('supplier', 'contract_type')
        status_filter = self.request.GET.get('status', '')
        type_filter = self.request.GET.get('type', '')
        search_query = self.request.GET.get('search', '')

        if status_filter:
            queryset = queryset.filter(status=status_filter)
        if type_filter:
            queryset = queryset.filter(contract_type_id=type_filter)
        if search_query:
            queryset = queryset.filter(
                Q(contract_number__icontains=search_query) |
                Q(contract_object__icontains=search_query) |
                Q(supplier__name__icontains=search_query)
            )
        return queryset

    def get_context_data(self, **kwargs):
        """Adiciona dados extras ao contexto para os filtros."""
        context = super().get_context_data(**kwargs)
        context['all_types'] = ContractType.objects.all()
        context['status_choices'] = Contract.StatusChoices.choices
        context['current_status'] = self.request.GET.get('status', '')
        context['current_type'] = self.request.GET.get('type', '')
        context['search_query'] = self.request.GET.get('search', '')
        return context

class ContractCreateView(CreateView):
    model = Contract
    template_name = 'contracts/contract_form.html'
    fields = [
        'contract_type', 'supplier', 'contract_number', 'contract_object',
        'status', 'start_date', 'duration_months', 'monthly_value',
        'payment_day', 'linked_assets', 'observations'
    ]
    success_url = reverse_lazy('contracts:contract_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Adicionar Novo Contrato"
        return context

class ContractUpdateView(UpdateView):
    model = Contract
    template_name = 'contracts/contract_form.html'
    fields = [
        'contract_type', 'supplier', 'contract_number', 'contract_object',
        'status', 'start_date', 'duration_months', 'monthly_value',
        'payment_day', 'linked_assets', 'observations'
    ]
    success_url = reverse_lazy('contracts:contract_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Editar Contrato"
        return context

class ContractDeleteView(DeleteView):
    model = Contract
    template_name = 'contracts/contract_confirm_delete.html'
    success_url = reverse_lazy('contracts:contract_list')
    context_object_name = 'contract'

class ContractDetailView(DetailView):
    model = Contract
    template_name = 'contracts/contract_detail.html'
    context_object_name = 'contract'