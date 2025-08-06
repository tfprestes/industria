# ==============================================================================
# core/admin.py - v2.1 (Correção do nome do campo em readonly_fields)
# ==============================================================================
"""
Configuração da interface de administração para a aplicação 'core'.
Esta versão inclui otimizações de performance (list_select_related, autocomplete_fields)
e melhorias de usabilidade (fieldsets, inlines, readonly_fields).
"""

from django.contrib import admin
from .models import (
    Asset, AssetType, Supplier, Unit, Sector, CostCenter, Attachment, Software
)

# ARQUITETO: Definindo Inlines para gerenciar modelos relacionados na página do Asset
class AttachmentInline(admin.TabularInline):
    """Permite adicionar/editar/remover anexos diretamente na página do Ativo."""
    model = Attachment
    extra = 1  # Quantidade de formulários extras para adicionar novos anexos

class SoftwareInline(admin.TabularInline):
    """Permite associar/desassociar softwares diretamente na página do Ativo."""
    model = Software.asset.through # Acessa a tabela ManyToMany intermediária
    verbose_name = "Software Instalado"
    verbose_name_plural = "Softwares Instalados"
    extra = 1
    autocomplete_fields = ['software'] # Adicionado para melhor UX

@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Identificação e Classificação', {
            'fields': ('asset_type', 'brand', 'model', 'status', 'serial_number', 'internal_tag', 'description')
        }),
        ('Associação e Responsabilidade', {
            'fields': ('assigned_unit', 'assigned_sector', 'assigned_cost_center', 'user', 'responsible', 'shared_with')
        }),
        ('Dados Financeiros e Contrato', {
            'fields': ('supplier', 'invoice_number', 'lease_value', 'cost', 'contract_duration_months')
        }),
        ('Datas do Ciclo de Vida', {
            'fields': ('receipt_date', 'invoice_date', 'lease_date', 'delivery_activation_date', 'contract_end_date', 'deactivation_date', 'exclusion_date')
        }),
        ('Especificações Técnicas', {
            'fields': ('operating_system', 'processor', 'memory_gb', 'office_version', 'ip_address')
        }),
        ('Campos de Celular', {
            'classes': ('collapse',),
            'fields': ('imei', 'phone_number'),
        }),
        ('Timestamps (Sistema)', {
            'fields': ('created_at', 'updated_at'),
        }),
    )
    list_select_related = ('asset_type', 'assigned_unit', 'user')
    list_display = ('__str__', 'status', 'asset_type', 'assigned_unit', 'user')
    list_filter = ('status', 'asset_type', 'assigned_unit', 'assigned_sector')
    search_fields = ('serial_number', 'internal_tag', 'brand', 'model', 'user__username', 'user__first_name', 'description')
    autocomplete_fields = ['user', 'responsible', 'shared_with', 'supplier', 'assigned_sector', 'assigned_cost_center']
    ordering = ('-created_at',)
    
    # ARQUITETO: CORREÇÃO APLICADA AQUI
    readonly_fields = ('created_at', 'updated_at', 'contract_end_date')

    inlines = [AttachmentInline, SoftwareInline]


@admin.register(AssetType)
class AssetTypeAdmin(admin.ModelAdmin):
    search_fields = ('name',)

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    search_fields = ('name', 'contact_person', 'contact_email')

@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    search_fields = ('name',)

@admin.register(Sector)
class SectorAdmin(admin.ModelAdmin):
    list_display = ('name', 'cost_center')
    list_filter = ('cost_center',)
    search_fields = ('name', 'cost_center__name')
    autocomplete_fields = ['cost_center']

@admin.register(CostCenter)
class CostCenterAdmin(admin.ModelAdmin):
    search_fields = ('name', 'code')

@admin.register(Attachment)
class AttachmentAdmin(admin.ModelAdmin):
    list_display = ('asset', 'file', 'description', 'uploaded_at')
    list_filter = ('asset',)
    search_fields = ('description', 'asset__internal_tag', 'asset__serial_number')
    autocomplete_fields = ['asset']

@admin.register(Software)
class SoftwareAdmin(admin.ModelAdmin):
    search_fields = ('name', 'version', 'license_key')
    # Adicionado para que o SoftwareInline possa usar autocomplete
    autocomplete_fields = ['asset']