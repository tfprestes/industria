# ==============================================================================
# core/forms.py - Novo arquivo para centralizar a definição de formulários
# ==============================================================================
"""
Módulo de formulários para a aplicação 'core'.
Define os formulários baseados em modelos (ModelForms) para garantir
segurança e manutenibilidade.
"""

from django import forms
from .models import Asset

class AssetForm(forms.ModelForm):
    """
    Formulário para a criação e edição de Ativos.
    Define explicitamente os campos que podem ser manipulados pelo usuário,
    evitando a vulnerabilidade de 'mass assignment' do uso de 'fields = "__all__"'.
    """
    class Meta:
        model = Asset
        # Lista explícita de todos os campos que o usuário pode preencher.
        # Se um novo campo for adicionado ao modelo, ele não aparecerá aqui
        # automaticamente, garantindo controle total.
        fields = [
            'asset_type', 'brand', 'model', 'status', 'serial_number', 
            'internal_tag', 'description', 'assigned_unit', 'assigned_sector', 
            'assigned_cost_center', 'user', 'responsible', 'shared_with', 
            'supplier', 'invoice_number', 'lease_value', 'cost', 
            'contract_duration_months', 'receipt_date', 'invoice_date', 
            'lease_date', 'delivery_activation_date', 'contract_end_date', 
            'deactivation_date', 'exclusion_date', 'operating_system', 
            'processor', 'memory_gb', 'office_version', 'ip_address', 'imei', 
            'phone_number'
        ]
        # Aqui você poderia adicionar widgets customizados, se necessário, por exemplo:
        # widgets = {
        #     'receipt_date': forms.DateInput(attrs={'type': 'date'}),
        # }