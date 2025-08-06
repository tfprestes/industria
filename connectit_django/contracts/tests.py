# ==============================================================================
# core/tests.py - v1 (Fundação da Suíte de Testes)
# ==============================================================================
"""
Suíte de testes para a aplicação 'core'.
Este arquivo serve como ponto de partida para garantir a qualidade e a
estabilidade do código, prevenindo regressões futuras.
"""

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Asset, AssetType, Unit, Sector, CostCenter, Supplier

# ARQUITETO: Testes são a rede de segurança que nos permite refatorar e
# adicionar funcionalidades com confiança.

class CoreViewsTestCase(TestCase):
    """
    Testa as views da aplicação 'core'.
    Cada teste é executado em um banco de dados temporário e isolado.
    """

    @classmethod
    def setUpTestData(cls):
        """
        ARQUITETO: Usamos setUpTestData para criar dados que serão compartilhados
        por todos os testes nesta classe. É mais eficiente que o setUp normal
        quando os dados não são modificados pelos testes.
        """
        # 1. Arrange: Criar os objetos necessários para os testes
        cls.user = User.objects.create_user(username='testuser', password='password123')
        cls.asset_type = AssetType.objects.create(name='Notebook')
        cls.unit = Unit.objects.create(name='Sede')
        cls.cost_center = CostCenter.objects.create(name='TI')
        cls.sector = Sector.objects.create(name='Desenvolvimento', cost_center=cls.cost_center)
        cls.supplier = Supplier.objects.create(name='Fornecedor Padrão')

        # Criar um ativo de teste
        cls.asset = Asset.objects.create(
            asset_type=cls.asset_type,
            brand='Dell',
            model='XPS 15',
            status='em_uso',
            assigned_unit=cls.unit,
            assigned_sector=cls.sector,
            assigned_cost_center=cls.cost_center,
            user=cls.user,
            cost=5000.00
        )

    def test_asset_model_str_representation(self):
        """
        Testa o método __str__ do modelo Asset.
        Garante que a representação em texto do objeto é clara e útil.
        """
        self.assertEqual(
            str(self.asset),
            f"{self.asset.brand} {self.asset.model} ({self.asset.serial_number or self.asset.internal_tag})"
        )
        print("✅ Teste de representação do modelo Asset passou.")

    def test_dashboard_view_loads_successfully(self):
        """
        Testa se a página do Dashboard carrega corretamente para um usuário logado.
        """
        # 2. Act: Fazer a requisição
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('core:dashboard'))

        # 3. Assert: Verificar o resultado
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/dashboard.html')
        print("✅ Teste de carregamento da DashboardView passou.")

    def test_asset_list_view_displays_asset(self):
        """
        Testa se a lista de ativos exibe o ativo que criamos.
        """
        # 2. Act
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('core:asset_list'))

        # 3. Assert
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/asset_list.html')
        self.assertContains(response, self.asset.brand) # Verifica se a marca 'Dell' está no HTML
        self.assertIn('assets', response.context) # Verifica se a variável 'assets' está no contexto
        self.assertEqual(len(response.context['assets']), 1) # Verifica se há exatamente 1 ativo na lista
        print("✅ Teste da AssetListView passou.")

    def test_asset_creation_flow(self):
        """
        Testa o fluxo completo de criação de um novo ativo.
        """
        self.client.login(username='testuser', password='password123')
        
        # 1. Arrange: Dados para o novo ativo
        new_asset_data = {
            'asset_type': self.asset_type.id,
            'brand': 'Apple',
            'model': 'MacBook Pro',
            'status': 'em_estoque',
            'assigned_unit': self.unit.id,
            'assigned_sector': self.sector.id,
            'assigned_cost_center': self.cost_center.id,
            'cost': 12000.00,
        }

        # 2. Act: Enviar a requisição POST para a view de criação
        url = reverse('core:asset_add')
        response = self.client.post(url, data=new_asset_data)

        # 3. Assert
        # Verifica se fomos redirecionados para a lista de ativos (código 302)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('core:asset_list'))

        # Verifica se o novo ativo realmente existe no banco de dados
        self.assertTrue(Asset.objects.filter(brand='Apple').exists())
        print("✅ Teste de fluxo de criação de Ativo passou.")