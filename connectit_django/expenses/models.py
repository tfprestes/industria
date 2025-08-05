# Em: expenses/models.py

from django.db import models
from core.models import Asset  # Importamos o modelo Asset da nossa outra app

class ExpenseType(models.Model):
    """
    Representa as categorias de despesas (ex: Manutenção, Software, Aquisição).
    """
    name = models.CharField(max_length=100, unique=True, verbose_name="Nome do Tipo de Despesa")
    description = models.TextField(blank=True, null=True, verbose_name="Descrição")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Tipo de Despesa"
        verbose_name_plural = "Tipos de Despesas"
        ordering = ['name']


class Expense(models.Model):
    """
    Representa uma despesa individual associada a um ativo.
    """
    description = models.CharField(max_length=255, verbose_name="Descrição da Despesa")
    expense_type = models.ForeignKey(ExpenseType, on_delete=models.PROTECT, verbose_name="Tipo de Despesa")
    
    # Relação com o ativo. Uma despesa pode ou não estar ligada a um ativo.
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE, null=True, blank=True, related_name='expenses', verbose_name="Ativo Associado")
    
    value = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor da Despesa")
    expense_date = models.DateField(verbose_name="Data da Despesa")
    
    invoice_attachment = models.FileField(upload_to='expense_invoices/', blank=True, null=True, verbose_name="Anexo (Nota Fiscal)")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Última Modificação")

    def __str__(self):
        return f"{self.description} - R$ {self.value}"

    class Meta:
        verbose_name = "Despesa"
        verbose_name_plural = "Despesas"
        ordering = ['-expense_date']