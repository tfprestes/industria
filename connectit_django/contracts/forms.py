# ==============================================================================
# contracts/forms.py - Novo arquivo para centralizar a definição de formulários
# ==============================================================================
"""
Módulo de formulários para a aplicação 'contracts'.
"""

from django import forms
from .models import Contract

class ContractForm(forms.ModelForm):
    """
    Formulário para a criação e edição de Contratos.
    Centraliza a lógica do formulário, permitindo futuras customizações
    de widgets e validações.
    """
    class Meta:
        model = Contract
        fields = [
            'contract_type', 'supplier', 'contract_number', 'contract_object',
            'status', 'start_date', 'duration_months', 'monthly_value',
            'payment_day', 'linked_assets', 'observations'
        ]
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'observations': forms.Textarea(attrs={'rows': 3}),
        }