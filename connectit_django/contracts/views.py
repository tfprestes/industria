# ==============================================================================
# contracts/views.py - v2 (Refatorado com ModelForms e Camada de Serviço)
# ==============================================================================
"""
Módulo de views para a aplicação 'contracts'.
Utiliza ModelForms para os formulários e invoca a camada de serviço
para executar lógicas de negócio complexas após salvar um contrato.
"""

from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from .models import Contract, ContractType
from .forms import ContractForm  # Importa o novo ModelForm
from .services import generate_payments_for_contract # Importa o nosso serviço!

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
    form_class = ContractForm # Usa o ModelForm que criamos
    template_name = 'contracts/contract_form.html'
    success_url = reverse_lazy('contracts:contract_list')

    def form_valid(self, form):
        """
        ARQUITETO: PONTO CRÍTICO DA REATORAÇÃO.
        Sobrescreve o método form_valid para chamar nosso serviço
        APÓS o contrato ser salvo com sucesso.
        """
        response = super().form_valid(form) # Primeiro, salva o contrato e obtém o objeto
        generate_payments_for_contract(self.object) # Agora, chama o serviço com o contrato recém-criado
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Adicionar Novo Contrato"
        return context

class ContractUpdateView(UpdateView):
    model = Contract
    form_class = ContractForm # Usa o ModelForm que criamos
    template_name = 'contracts/contract_form.html'
    success_url = reverse_lazy('contracts:contract_list')
    
    def form_valid(self, form):
        """
        ARQUITETO: Também aplicamos a lógica aqui para re-gerar as parcelas
        caso um contrato seja atualizado (ex: mudança na duração ou valor).
        """
        response = super().form_valid(form)
        generate_payments_for_contract(self.object)
        return response

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