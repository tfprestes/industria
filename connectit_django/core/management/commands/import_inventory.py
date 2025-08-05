# Em: inventory/management/commands/import_inventory.py
import csv
from django.core.management.base import BaseCommand
from inventory.models import StockItem, InventoryItemType
from core.models import Supplier

class Command(BaseCommand):
    help = 'Importa itens de inventário de um arquivo CSV.'

    def add_arguments(self, parser):
        parser.add_argument('csv_file_path', type=str)

    def handle(self, *args, **options):
        csv_file_path = options['csv_file_path']
        self.stdout.write(f"Importando itens de inventário de: {csv_file_path}")

        with open(csv_file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                firestore_id = row.get('id_firestore')
                if not firestore_id: continue

                # --- Busca pelos objetos relacionados ---
                item_type = None
                if row.get('itemType'):
                    try:
                        item_type = InventoryItemType.objects.get(name=row['itemType'].strip())
                    except InventoryItemType.DoesNotExist:
                        self.stdout.write(self.style.WARNING(f"AVISO: Categoria '{row['itemType']}' não encontrada."))

                supplier = None
                if row.get('supplierId'):
                    try:
                        supplier = Supplier.objects.get(firestore_id=row['supplierId'])
                    except Supplier.DoesNotExist:
                        self.stdout.write(self.style.WARNING(f"AVISO: Fornecedor com firestore_id '{row['supplierId']}' não encontrado."))

                # --- Criação ou Atualização do Item ---
                obj, created = StockItem.objects.update_or_create(
                    firestore_id=firestore_id,
                    defaults={
                        'item_name': row.get('itemName', 'Nome em falta'),
                        'item_type': item_type,
                        'quantity': int(row.get('quantity') or 0),
                        'min_stock_level': int(row.get('minStockLevel') or 0),
                        'unit_of_measure': row.get('unitOfMeasure', ''),
                        'location_description': row.get('locationDescription', ''),
                        'supplier': supplier,
                    }
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f"Item '{obj.item_name}' criado."))
                else:
                    self.stdout.write(self.style.WARNING(f"Item '{obj.item_name}' atualizado."))
        
        self.stdout.write(self.style.SUCCESS('Importação de inventário concluída.'))