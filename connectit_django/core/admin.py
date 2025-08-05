# Em: core/admin.py

from django.contrib import admin
from .models import (
    Asset, AssetType, Supplier, Unit, Sector, CostCenter, Attachment
)

@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'serial_number', 'status', 'asset_type', 'assigned_unit', 'user')
    list_filter = ('status', 'asset_type', 'assigned_unit', 'assigned_sector')
    search_fields = ('serial_number', 'internal_tag', 'brand', 'model', 'user', 'description')
    ordering = ('-created_at',)

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
    # CORREÇÃO AQUI: Trocamos 'unit' por 'cost_center'
    list_display = ('name', 'cost_center')
    list_filter = ('cost_center',)
    search_fields = ('name',)

@admin.register(CostCenter)
class CostCenterAdmin(admin.ModelAdmin):
    search_fields = ('name', 'code')

@admin.register(Attachment)
class AttachmentAdmin(admin.ModelAdmin):
    list_display = ('asset', 'file', 'description', 'uploaded_at')
    list_filter = ('asset',)
    search_fields = ('description',)