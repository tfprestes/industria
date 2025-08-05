# Em: expenses/admin.py

from django.contrib import admin
from .models import Expense, ExpenseType

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('description', 'expense_type', 'value', 'expense_date', 'asset')
    list_filter = ('expense_type', 'expense_date', 'asset__assigned_unit')
    search_fields = ('description', 'asset__serial_number', 'asset__internal_tag')
    autocomplete_fields = ['asset']

@admin.register(ExpenseType)
class ExpenseTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)