# Em: inventory/management/commands/import_inventory_types.py
import csv
from django.core.management.base import BaseCommand
from inventory.models import InventoryItemType

class Command(BaseCommand):
    help = 'Extrai e cria tipos de item de inventário a partir de um arquivo CSV de inventário.'

    def add_arguments(self, parser):
        parser.add_argument('csv_file_path', type=str)

    def handle(self, *args, **options):
        csv_file_path = options['csv_file_path']
        self.stdout.write("Extraindo tipos de item...")
        
        item_types = set()
        with open(csv_file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                item_type_name = row.get('itemType')
                if item_type_name:
                    item_types.add(item_type_name.strip())
        
        for type_name in sorted(list(item_types)):
            obj, created = InventoryItemType.objects.get_or_create(name=type_name)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Categoria '{type_name}' criada."))
        
        self.stdout.write(self.style.SUCCESS('Criação de categorias concluída.'))