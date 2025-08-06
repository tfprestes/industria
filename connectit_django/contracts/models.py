# ==============================================================================
# contracts/models.py - v2 (Corrigido e Refatorado pelo Arquiteto de Software)
# ==============================================================================
"""
Módulo de modelos para a aplicação 'contracts' do ConnectIT.
Contém as definições de modelos para tipos de contrato, contratos e pagamentos agendados.
A lógica de negócio para geração de parcelas foi movida para contracts/services.py.
"""

from django.db import models
from dateutil.relativedelta import relativedelta
from core.models import Asset, Supplier

class ContractType(models.Model):
    firestore_id = models.CharField(max_length=50, unique=True, null=True, blank=True, db_index=True)
    name = models.CharField(max_length=100, unique=True, verbose_name="Nome do Tipo de Contrato")
    description = models.TextField(blank=True, null=True, verbose_name="Descrição")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Tipo de Contrato"
        verbose_name_plural = "Tipos de Contratos"
        ordering = ['name']

class Contract(models.Model):
    firestore_id = models.CharField(max_length=50, unique=True, null=True, blank=True, db_index=True)

    class StatusChoices(models.TextChoices):
        PAID = 'paid', 'Pago'
        WAITING = 'waiting', 'Aguardando'
        COMPLETED = 'completed', 'Concluído'
        ACTIVE = 'ativo', 'Ativo'
        INACTIVE = 'inativo', 'Inativo'
        FINISHED = 'encerrado', 'Encerrado'
        CANCELED = 'cancelado', 'Cancelado'

    contract_type = models.ForeignKey(ContractType, on_delete=models.PROTECT, verbose_name="Tipo de Contrato")
    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT, verbose_name="Fornecedor")
    contract_number = models.CharField(max_length=100, blank=True, null=True, verbose_name="Número do Contrato")
    contract_object = models.TextField(verbose_name="Objeto do Contrato")
    status = models.CharField(
        max_length=20,
        choices=StatusChoices.choices,
        default=StatusChoices.ACTIVE,
        verbose_name="Status",
    )
    start_date = models.DateField(verbose_name="Data de Início", null=True, blank=True)
    duration_months = models.PositiveIntegerField(verbose_name="Duração (meses)", null=True, blank=True)
    end_date = models.DateField(verbose_name="Data de Fim", blank=True, null=True)
    monthly_value = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor Mensal")
    payment_day = models.PositiveIntegerField(
        verbose_name="Dia do Pagamento no Mês", help_text="Dia do mês em que a fatura vence (1-31)"
    )
    linked_assets = models.ManyToManyField(Asset, blank=True, verbose_name="Ativos Vinculados")
    observations = models.TextField(blank=True, null=True, verbose_name="Observações")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Contrato {self.contract_number or self.id} - {self.supplier.name}"

    def save(self, *args, **kwargs):
        # A única lógica que permanece no save é o cálculo da data de fim,
        # pois é uma propriedade intrínseca do próprio contrato.
        if self.start_date and self.duration_months:
            self.end_date = self.start_date + relativedelta(months=self.duration_months)
        else:
            self.end_date = None
        
        # A lógica de criação de pagamentos foi REMOVIDA daqui.
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Contrato"
        verbose_name_plural = "Contratos"
        ordering = ['-start_date']

class ScheduledPayment(models.Model):
    class StatusChoices(models.TextChoices):
        WAITING = 'waiting', 'Aguardando'
        PAID = 'pago', 'Pago'
        OVERDUE = 'em_atraso', 'Em Atraso'

    contract = models.ForeignKey(
        Contract,
        on_delete=models.CASCADE,
        related_name='payments',
        verbose_name="Contrato"
    )
    due_date = models.DateField(verbose_name="Data de Vencimento")
    value = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor")
    status = models.CharField(
        max_length=20,
        choices=StatusChoices.choices,
        default=StatusChoices.WAITING,
        verbose_name="Status"
    )
    payment_date = models.DateField(blank=True, null=True, verbose_name="Data de Pagamento Efetivo")
    description = models.CharField(max_length=255, blank=True, null=True, verbose_name="Descrição da Parcela")

    def __str__(self):
        return f"Parcela de {self.due_date.strftime('%B/%Y')} - Contrato {self.contract.id}"

    class Meta:
        verbose_name = "Pagamento Agendado"
        verbose_name_plural = "Pagamentos Agendados"
        ordering = ['due_date']