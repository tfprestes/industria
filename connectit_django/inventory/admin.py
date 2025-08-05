# Em: inventory/admin.py

from django.contrib import admin
from .models import StockItem, InventoryItemType

@admin.register(StockItem)
class StockItemAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'item_type', 'quantity', 'min_stock_level', 'location_description')
    list_filter = ('item_type', 'location_description')
    search_fields = ('item_name', 'location_description')
    autocomplete_fields = ['supplier']
    ordering = ('item_name',)

@admin.register(InventoryItemType)
class InventoryItemTypeAdmin(admin.ModelAdmin):
    search_fields = ('name',)