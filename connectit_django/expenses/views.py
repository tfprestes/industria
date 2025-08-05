# connectit_django/expenses/views.py
from django.shortcuts import render
from .models import Expense

def expense_list(request):
    """
    Exibe uma lista de todas as despesas.
    """
    expenses = Expense.objects.all()
    return render(request, 'expenses/expense_list.html', {'expenses': expenses})
