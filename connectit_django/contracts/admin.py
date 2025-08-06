# ==============================================================================
# contracts/admin.py - v2 (Refatorado para Performance e Usabilidade)
# ==============================================================================
"""
Configuração da interface de administração para a aplicação 'contracts'.
Esta versão adiciona fieldsets para melhor organização e otimiza a listagem
de pagamentos com list_editable e list_select_related.
"""

from django.contrib import admin
from .models import Contract, ContractType, ScheduledPayment

class ScheduledPaymentInline(admin.TabularInline):
    """
    ARQUITETO: Excelente implementação!
    Atua como um 'relatório' somente leitura das parcelas na página do contrato,
    respeitando a regra de que elas são geradas por um serviço.
    """
    model = ScheduledPayment
    extra = 0
    readonly_fields = ('due_date', 'value', 'status', 'payment_date', 'description')
    can_delete = False

    def has_add_permission(self, request, obj=None):
        return False

@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    # ARQUITETO: Adicionando fieldsets para organizar a grande quantidade de campos.
    fieldsets = (
        ('Informações Principais', {
            'fields': ('contract_type', 'supplier', 'contract_number', 'contract_object', 'status')
        }),
        ('Datas e Duração', {
            'fields': ('start_date', 'duration_months', 'end_date')
        }),
        ('Valores e Pagamento', {
            'fields': ('monthly_value', 'payment_day')
        }),
        ('Vínculos e Observações', {
            'fields': ('linked_assets', 'observations')
        }),
    )

    list_display = ('__str__', 'contract_type', 'start_date', 'end_date', 'monthly_value', 'status')
    list_filter = ('status', 'contract_type', 'supplier')
    search_fields = ('contract_number', 'contract_object', 'supplier__name')
    autocomplete_fields = ['supplier', 'linked_assets']
    
    # ARQUITETO: Protegendo o campo 'end_date' que é calculado automaticamente.
    readonly_fields = ('end_date', 'created_at', 'updated_at')

    inlines = [ScheduledPaymentInline]

@admin.register(ContractType)
class ContractTypeAdmin(admin.ModelAdmin):
    search_fields = ('name',)

@admin.register(ScheduledPayment)
class ScheduledPaymentAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'status', 'due_date', 'value', 'payment_date')
    list_filter = ('status', 'due_date')
    search_fields = ('contract__contract_number', 'description')
    
    # ARQUITETO: Otimização de performance para evitar N+1 queries na listagem.
    list_select_related = ('contract', 'contract__supplier')
    
    # ARQUITETO: Melhoria de usabilidade. Permite alterar o status e a data
    # diretamente na lista, sem precisar abrir cada parcela individualmente.
    list_editable = ('status', 'payment_date')