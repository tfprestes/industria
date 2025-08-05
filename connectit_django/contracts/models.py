# ==============================================================================
# contracts/models.py - Refatorado e Corrigido como Arquiteto de Software Sênior
# ==============================================================================
"""
Módulo de modelos para a aplicação 'contracts' do ConnectIT.
Contém as definições de modelos para tipos de contrato, contratos e pagamentos agendados.
"""

from django.db import models
from dateutil.relativedelta import relativedelta
from core.models import Asset, Supplier  # Assegura que Asset e Supplier são importados de core.models

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
        # Lógica robusta para calcular a data de fim
        if self.start_date and self.duration_months:
            self.end_date = self.start_date + relativedelta(months=self.duration_months)
        else:
            self.end_date = None

        is_new = self._state.adding
        super().save(*args, **kwargs)

        # Lógica para gerar as parcelas
        if is_new and self.start_date and self.duration_months:
            # Limpa parcelas antigas se existirem
            self.payments.all().delete()
            for i in range(self.duration_months):
                due_date = self.start_date + relativedelta(months=i)
                # Define o dia correto de vencimento dentro do mês
                try:
                    due_date = due_date.replace(day=self.payment_day)
                except ValueError:
                    # Ajusta para o último dia do mês se o dia não existir
                    last_day_of_month = (due_date.replace(day=28) + relativedelta(days=4)).replace(day=1) - relativedelta(days=1)
                    due_date = last_day_of_month

                ScheduledPayment.objects.create(
                    contract=self,
                    due_date=due_date,
                    value=self.monthly_value,
                    description=f"Parcela {i + 1} de {self.duration_months} - Contrato {self.contract_number or self.id}"
                )

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
    # Campo 'description' adicionado para resolver AttributeError no dashboard
    description = models.CharField(max_length=255, blank=True, null=True, verbose_name="Descrição da Parcela")

    def __str__(self):
        return f"Parcela de {self.due_date.strftime('%B/%Y')} - Contrato {self.contract.id}"

    class Meta:
        verbose_name = "Pagamento Agendado"
        verbose_name_plural = "Pagamentos Agendados"
        ordering = ['due_date']
