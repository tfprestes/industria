# Em: inventory/models.py

from django.db import models
from core.models import Supplier # Importamos o Fornecedor da nossa app 'core'

class InventoryItemType(models.Model):
    """ Representa as categorias dos itens em stock (ex: Cabo, Periférico). """
    name = models.CharField(max_length=100, unique=True, verbose_name="Nome da Categoria")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Categoria de Item de Inventário"
        verbose_name_plural = "Categorias de Itens de Inventário"
        ordering = ['name']

class StockItem(models.Model):
    """ Representa um item individual em stock/inventário. """
    firestore_id = models.CharField(max_length=50, unique=True, null=True, db_index=True)
    item_name = models.CharField(max_length=255, verbose_name="Nome do Item")
    item_type = models.ForeignKey(InventoryItemType, on_delete=models.SET_NULL, null=True, verbose_name="Categoria")
    
    quantity = models.PositiveIntegerField(default=0, verbose_name="Quantidade em Stock")
    min_stock_level = models.PositiveIntegerField(default=0, verbose_name="Nível Mínimo de Stock")
    
    unit_of_measure = models.CharField(max_length=50, blank=True, verbose_name="Unidade de Medida")
    location_description = models.CharField(max_length=255, blank=True, verbose_name="Descrição da Localização")
    
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Fornecedor Padrão")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.item_name

    class Meta:
        verbose_name = "Item de Inventário"
        verbose_name_plural = "Itens de Inventário"
        ordering = ['item_name']