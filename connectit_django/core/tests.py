# ==============================================================================
# core/tests.py - v2 (Estrutura de Teste Refatorada e Final)
# ==============================================================================
"""
Suíte de testes para a aplicação 'core'.
Testes são separados por responsabilidade (Modelos, Views, etc.) para maior
clareza e manutenibilidade.
"""

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Asset, AssetType, Unit, Sector, CostCenter, Supplier

# ARQUITETO: Uma suíte de testes bem estruturada é um ativo de software.
# Separar testes por funcionalidade (Modelos, Views, Forms, Services) é uma
# prática recomendada que escala bem conforme o projeto cresce.

class CoreModelTests(TestCase):
    """Testa os modelos da aplicação 'core'."""

    @classmethod
    def setUpTestData(cls):
        """Cria os dados base que não serão modificados durante os testes."""
        cls.asset_type = AssetType.objects.create(name='Desktop')
        cls.unit = Unit.objects.create(name='Matriz')
        cls.cost_center = CostCenter.objects.create(name='Operacional')
        cls.sector = Sector.objects.create(name='Atendimento', cost_center=cls.cost_center)
        cls.user = User.objects.create_user(username='testuser.model', password='password123')

    def test_asset_creation(self):
        """Verifica se um objeto Asset pode ser criado com sucesso."""
        asset = Asset.objects.create(
            asset_type=self.asset_type,
            brand='HP',
            model='ProDesk',
            assigned_unit=self.unit,
            assigned_sector=self.sector,
            assigned_cost_center=self.cost_center,
            user=self.user
        )
        self.assertIsInstance(asset, Asset)
        self.assertEqual(str(asset), f"{asset.brand} {asset.model} ({asset.serial_number or asset.internal_tag})")


class CoreViewTests(TestCase):
    """Testa as views da aplicação 'core'."""

    @classmethod
    def setUpTestData(cls):
        """Cria dados base para os testes de view."""
        cls.user = User.objects.create_user(username='testuser.view', password='password123')
        asset_type = AssetType.objects.create(name='Notebook')
        unit = Unit.objects.create(name='Filial')
        cost_center = CostCenter.objects.create(name='Administrativo')
        sector = Sector.objects.create(name='RH', cost_center=cost_center)

        cls.asset = Asset.objects.create(
            asset_type=asset_type,
            brand='Dell',
            model='XPS 15',
            assigned_unit=unit,
            assigned_sector=sector,
            assigned_cost_center=cost_center,
            user=cls.user
        )

    def test_dashboard_view_authenticated(self):
        """Verifica se o dashboard carrega para um usuário autenticado."""
        self.client.login(username='testuser.view', password='password123')
        response = self.client.get(reverse('core:dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/dashboard.html')

    def test_asset_list_view_displays_data(self):
        """Verifica se a lista de ativos exibe o ativo criado."""
        self.client.login(username='testuser.view', password='password123')
        response = self.client.get(reverse('core:asset_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.asset.brand)
        self.assertEqual(len(response.context['assets']), 1)