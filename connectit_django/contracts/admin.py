# Em: contracts/admin.py

from django.contrib import admin
from .models import Contract, ContractType, ScheduledPayment

class ScheduledPaymentInline(admin.TabularInline):
    """Permite visualizar e editar as parcelas diretamente na página do contrato."""
    model = ScheduledPayment
    extra = 0  # Não mostra formulários de parcela em branco por padrão
    readonly_fields = ('due_date', 'value') # Impede a edição de parcelas geradas automaticamente
    can_delete = False # Impede a exclusão de parcelas

    def has_add_permission(self, request, obj=None):
        return False # Desabilita o botão "Adicionar outro Pagamento Agendado"

@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ('contract_number', 'supplier', 'contract_type', 'start_date', 'end_date', 'monthly_value', 'status')
    list_filter = ('status', 'contract_type', 'supplier')
    search_fields = ('contract_number', 'contract_object', 'supplier__name')
    autocomplete_fields = ['supplier', 'linked_assets']
    inlines = [ScheduledPaymentInline] # Adiciona as parcelas na página do contrato

@admin.register(ContractType)
class ContractTypeAdmin(admin.ModelAdmin):
    search_fields = ('name',)

@admin.register(ScheduledPayment)
class ScheduledPaymentAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'status', 'due_date', 'value', 'payment_date')
    list_filter = ('status', 'due_date')
    search_fields = ('contract__contract_number',)