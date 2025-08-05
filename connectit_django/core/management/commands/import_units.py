# Em: core/management/commands/import_units.py
import csv
from django.core.management.base import BaseCommand
from core.models import Unit

class Command(BaseCommand):
    help = 'Importa unidades a partir de um arquivo CSV.'

    def add_arguments(self, parser):
        parser.add_argument('csv_file_path', type=str)

    def handle(self, *args, **options):
        csv_file_path = options['csv_file_path']
        self.stdout.write(f"Importando Unidades de: {csv_file_path}")
        with open(csv_file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                obj, created = Unit.objects.update_or_create(
                    name=row['name'],
                    defaults={'firestore_id': row['id_firestore']}
                )
                if created: self.stdout.write(self.style.SUCCESS(f"Unidade '{obj.name}' criada."))
                else: self.stdout.write(self.style.WARNING(f"Unidade '{obj.name}' atualizada."))
        self.stdout.write(self.style.SUCCESS('Importação de Unidades concluída.'))