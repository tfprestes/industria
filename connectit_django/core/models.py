# ==============================================================================
# core/models.py - v3 (Versão Final Pós-Refatoração)
# O modelo duplicado 'InventoryItem' foi removido.
# ==============================================================================
"""
Módulo de modelos para a aplicação 'core' do ConnectIT.
Contém as definições de modelos principais e de suporte ao ecossistema.
"""

import os
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# O campo 'firestore_id' mapeia dados antigos durante a importação.
# É uma solução pragmática e temporária. Planejar remoção após migração.

class AssetType(models.Model):
    firestore_id = models.CharField(max_length=50, unique=True, null=True, blank=True, db_index=True)
    name = models.CharField(max_length=100, unique=True, verbose_name="Nome do Tipo")
    description = models.TextField(blank=True, null=True, verbose_name="Descrição")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Tipo de Ativo"
        verbose_name_plural = "Tipos de Ativos"
        ordering = ['name']


class Supplier(models.Model):
    firestore_id = models.CharField(max_length=50, unique=True, null=True, blank=True, db_index=True)
    name = models.CharField(max_length=200, verbose_name="Nome do Fornecedor")
    contact_person = models.CharField(max_length=100, blank=True, null=True, verbose_name="Pessoa de Contato")
    contact_email = models.EmailField(blank=True, null=True, verbose_name="E-mail de Contato")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Fornecedor"
        verbose_name_plural = "Fornecedores"
        ordering = ['name']


class Unit(models.Model):
    firestore_id = models.CharField(max_length=50, unique=True, null=True, blank=True, db_index=True)
    name = models.CharField(max_length=100, unique=True, verbose_name="Nome da Unidade")

    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name = "Unidade"
        verbose_name_plural = "Unidades"
        ordering = ['name']


class CostCenter(models.Model):
    firestore_id = models.CharField(max_length=50, unique=True, null=True, blank=True, db_index=True)
    name = models.CharField(max_length=100, unique=True, verbose_name="Nome do Centro de Custo")
    code = models.CharField(max_length=50, unique=True, blank=True, null=True, verbose_name="Código")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Centro de Custo"
        verbose_name_plural = "Centros de Custo"
        ordering = ['name']


class Sector(models.Model):
    firestore_id = models.CharField(max_length=50, unique=True, null=True, blank=True, db_index=True)
    name = models.CharField(max_length=100, unique=True, verbose_name="Nome do Setor")
    cost_center = models.ForeignKey(CostCenter, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Centro de Custo")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Setor"
        verbose_name_plural = "Setores"
        ordering = ['name']


class Asset(models.Model):
    """
    Representa o ativo principal do sistema (computadores, celulares, etc.).
    É a entidade central que agrega a maioria das informações.
    """
    firestore_id = models.CharField(max_length=50, unique=True, null=True, blank=True, db_index=True)
    
    class StatusChoices(models.TextChoices):
        WAITING = 'waiting', _('Aguardando')
        COMPLETED = 'completed', _('Concluído')
        IN_USE = 'em_uso', _('Em Uso')
        IN_STOCK = 'em_estoque', _('Em Estoque')
        IN_MAINTENANCE = 'em_manutencao', _('Em Manutenção')
        DISCARDED = 'descartado', _('Descartado')

    # --- Identificação e Classificação ---
    asset_type = models.ForeignKey(AssetType, on_delete=models.PROTECT, verbose_name="Tipo de Ativo")
    brand = models.CharField(max_length=100, verbose_name="Marca")
    model = models.CharField(max_length=100, verbose_name="Modelo")
    status = models.CharField(max_length=20, choices=StatusChoices.choices, default=StatusChoices.IN_STOCK, verbose_name="Status")
    serial_number = models.CharField(max_length=100, unique=True, null=True, blank=True, verbose_name="Número de Série")
    internal_tag = models.CharField(max_length=50, unique=True, null=True, blank=True, verbose_name="Etiqueta Interna")
    description = models.TextField(blank=True, null=True, verbose_name="Descrição/Observações")

    # --- Associação e Responsabilidade ---
    assigned_unit = models.ForeignKey(Unit, on_delete=models.PROTECT, verbose_name="Unidade Designada")
    assigned_sector = models.ForeignKey(Sector, on_delete=models.PROTECT, verbose_name="Setor Designado")
    assigned_cost_center = models.ForeignKey(CostCenter, on_delete=models.PROTECT, verbose_name="Centro de Custo")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_assets', verbose_name="Usuário Designado")
    responsible = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='responsible_for_assets', verbose_name="Responsável Técnico")
    shared_with = models.ManyToManyField(User, blank=True, related_name='shared_assets', verbose_name="Compartilhado Com")

    # --- Dados Financeiros e Contrato ---
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Fornecedor")
    invoice_number = models.CharField(max_length=50, blank=True, null=True, verbose_name="Número da Nota Fiscal")
    lease_value = models.DecimalField(max_digits=10, decimal_places=2, default=0.0, verbose_name="Valor de Locação/Compra")
    cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.0, verbose_name="Custo Total do Ativo")
    contract_duration_months = models.IntegerField(blank=True, null=True, verbose_name="Duração do Contrato (meses)")

    # --- Datas do Ciclo de Vida ---
    receipt_date = models.DateTimeField(blank=True, null=True, verbose_name="Data de Recebimento")
    invoice_date = models.DateTimeField(blank=True, null=True, verbose_name="Data da Nota Fiscal")
    lease_date = models.DateTimeField(blank=True, null=True, verbose_name="Data de Locação/Início do Contrato")
    delivery_activation_date = models.DateTimeField(blank=True, null=True, verbose_name="Data de Ativação/Entrega")
    contract_end_date = models.DateTimeField(blank=True, null=True, verbose_name="Data de Fim do Contrato")
    deactivation_date = models.DateTimeField(blank=True, null=True, verbose_name="Data de Desativação")
    exclusion_date = models.DateTimeField(blank=True, null=True, verbose_name="Data de Exclusão/Baixa")

    # --- Especificações Técnicas ---
    operating_system = models.CharField(max_length=100, blank=True, null=True, verbose_name="Sistema Operacional")
    processor = models.CharField(max_length=100, blank=True, null=True, verbose_name="Processador")
    memory_gb = models.IntegerField(blank=True, null=True, verbose_name="Memória (GB)")
    office_version = models.CharField(max_length=50, blank=True, null=True, verbose_name="Versão do Office")
    ip_address = models.GenericIPAddressField(protocol='both', blank=True, null=True, verbose_name="Endereço IP")
    
    # --- Campos de Celular ---
    imei = models.CharField(max_length=15, blank=True, null=True, verbose_name="IMEI")
    phone_number = models.CharField(max_length=20, blank=True, null=True, verbose_name="Número de Telefone")
    
    # --- Timestamps ---
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Última Modificação")

    def __str__(self):
        return f"{self.brand} {self.model} ({self.serial_number or self.internal_tag})"

    class Meta:
        verbose_name = "Ativo"
        verbose_name_plural = "Ativos"
        ordering = ['-created_at']


def asset_attachment_path(instance, filename):
    return f'asset_attachments/{instance.asset.id}/{filename}'


class Attachment(models.Model):
    asset = models.ForeignKey(Asset, related_name='attachments', on_delete=models.CASCADE, verbose_name="Ativo")
    file = models.FileField(upload_to=asset_attachment_path, verbose_name="Arquivo")
    description = models.CharField(max_length=255, blank=True, null=True, verbose_name="Descrição")
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de Upload")

    def __str__(self):
        return f"Anexo para '{self.asset}' - {os.path.basename(self.file.name)}"

    class Meta:
        verbose_name = "Anexo"
        verbose_name_plural = "Anexos"


class SoftwareCategory(models.Model):
    """
    Categorias para agrupar softwares (ex: Produtividade, Segurança, Sistema Operacional).
    """
    firestore_id = models.CharField(max_length=50, unique=True, null=True, blank=True, db_index=True)
    name = models.CharField(max_length=100, unique=True, verbose_name="Nome da Categoria")
    description = models.TextField(blank=True, null=True, verbose_name="Descrição")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Categoria de Software"
        verbose_name_plural = "Categorias de Software"
        ordering = ['name']


class Software(models.Model):
    """
    Representa um software ou licença de software que pode ser associado a um ou mais ativos.
    """
    firestore_id = models.CharField(max_length=50, unique=True, null=True, blank=True, db_index=True)
    name = models.CharField(max_length=200, verbose_name="Nome do Software")
    version = models.CharField(max_length=50, blank=True, null=True, verbose_name="Versão")
    category = models.ForeignKey(SoftwareCategory, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Categoria")
    license_key = models.CharField(max_length=255, unique=True, null=True, blank=True, verbose_name="Chave de Licença")
    asset = models.ManyToManyField(Asset, blank=True, related_name='installed_software', verbose_name="Ativos Instalados Em")
    purchase_date = models.DateField(blank=True, null=True, verbose_name="Data de Compra")
    expiration_date = models.DateField(blank=True, null=True, verbose_name="Data de Expiração")
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Fornecedor")

    def __str__(self):
        return f"{self.name} v{self.version or 'N/A'}"

    class Meta:
        verbose_name = "Software"
        verbose_name_plural = "Softwares"
        ordering = ['name']


class FinancialRecord(models.Model):
    """
    Representa um registro financeiro genérico (receita ou despesa) para o dashboard.
    """
    class RecordTypeChoices(models.TextChoices):
        REVENUE = 'receita', _('Receita')
        EXPENSE = 'despesa', _('Despesa')
        
    firestore_id = models.CharField(max_length=50, unique=True, null=True, blank=True, db_index=True)
    date = models.DateField(verbose_name="Data do Registro")
    type = models.CharField(max_length=10, choices=RecordTypeChoices.choices, verbose_name="Tipo de Registro")
    value = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor")
    description = models.TextField(blank=True, null=True, verbose_name="Descrição")
    cost_center = models.ForeignKey(CostCenter, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Centro de Custo Associado")
    
    def __str__(self):
        return f"{self.get_type_display()} - R$ {self.value} em {self.date}"

    class Meta:
        verbose_name = "Registro Financeiro"
        verbose_name_plural = "Registros Financeiros"
        ordering = ['-date']