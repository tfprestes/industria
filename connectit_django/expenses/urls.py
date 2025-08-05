# connectit_django/expenses/urls.py
from django.urls import path
from .views import expense_list

app_name = 'expenses'

urlpatterns = [
    path('', expense_list, name='expense_list'),
    # outras rotas de despesas aqui, se existirem
]