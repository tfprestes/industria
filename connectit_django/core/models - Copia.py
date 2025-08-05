# Em: core/models.py

from django.db import models
from django.contrib.auth.models import User

# --- Modelos de Apoio (Entidades Relacionadas) ---

class AssetType(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Nome do Tipo")
    description = models.TextField(blank=True, null=True, verbose_name="Descrição")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Tipo de Ativo"
        verbose_name_plural = "Tipos de Ativos"
        ordering = ['name']

class Supplier(models.Model):
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
    name = models.CharField(max_length=100, unique=True, verbose_name="Nome da Unidade")

    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name = "Unidade"
        verbose_name_plural = "Unidades"
        ordering = ['name']

class Sector(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Nome do Setor")
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, verbose_name="Unidade")

    def __str__(self):
        return f"{self.name} ({self.unit.name})"

    class Meta:
        verbose_name = "Setor"
        verbose_name_plural = "Setores"
        ordering = ['name']

class CostCenter(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Nome do Centro de Custo")
    code = models.CharField(max_length=50, unique=True, blank=True, null=True, verbose_name="Código")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Centro de Custo"
        verbose_name_plural = "Centros de Custo"
        ordering = ['name']
        
# --- Modelo Principal de Ativo ---

class Asset(models.Model):
    
    class StatusChoices(models.TextChoices):
        IN_USE = 'em_uso', 'Em Uso'
        IN_STOCK = 'em_estoque', 'Em Estoque'
        IN_MAINTENANCE = 'em_manutencao', 'Em Manutenção'
        DISCARDED = 'descartado', 'Descartado'

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
    user = models.CharField(max_length=100, blank=True, null=True, verbose_name="Usuário")
    responsible = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='responsible_for_assets', verbose_name="Responsável Técnico")
    shared_with = models.ManyToManyField(User, blank=True, related_name='shared_assets', verbose_name="Compartilhado Com")

    # --- Dados Financeiros e Contrato ---
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Fornecedor")
    invoice_number = models.CharField(max_length=50, blank=True, null=True, verbose_name="Número da Nota Fiscal")
    lease_value = models.DecimalField(max_digits=10, decimal_places=2, default=0.0, verbose_name="Valor de Locação/Compra")
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
    memory = models.CharField(max_length=50, blank=True, null=True, verbose_name="Memória RAM")
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

# Modelo para lidar com os anexos
def asset_attachment_path(instance, filename):
    # O arquivo será salvo em MEDIA_ROOT/asset_attachments/<asset_id>/<filename>
    return f'asset_attachments/{instance.asset.id}/{filename}'

class Attachment(models.Model):
    asset = models.ForeignKey(Asset, related_name='attachments', on_delete=models.CASCADE, verbose_name="Ativo")
    file = models.FileField(upload_to=asset_attachment_path, verbose_name="Arquivo")
    description = models.CharField(max_length=255, blank=True, null=True, verbose_name="Descrição")
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de Upload")

    def __str__(self):
        return f"Anexo para {self.asset.name} - {self.file.name}"

    class Meta:
        verbose_name = "Anexo"
        verbose_name_plural = "Anexos"