# Em: core/management/commands/import_suppliers.py
import csv
from django.core.management.base import BaseCommand
from core.models import Supplier

class Command(BaseCommand):
    help = 'Importa ou atualiza fornecedores a partir de um arquivo CSV.'

    def add_arguments(self, parser):
        parser.add_argument('csv_file_path', type=str, help='O caminho para o arquivo suppliers.csv')

    def handle(self, *args, **options):
        csv_file_path = options['csv_file_path']
        self.stdout.write(self.style.SUCCESS(f"Iniciando a importação de Fornecedores de: {csv_file_path}"))

        with open(csv_file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                firestore_id = row.get('id_firestore')
                if not firestore_id:
                    self.stdout.write(self.style.WARNING("Linha ignorada: id_firestore em falta."))
                    continue

                obj, created = Supplier.objects.update_or_create(
                    firestore_id=firestore_id,
                    defaults={
                        'name': row.get('name', 'Nome em falta'),
                        'contact_email': row.get('email'),
                        # Adicione outros campos do seu CSV aqui se necessário
                        # 'cnpj': row.get('cnpj'),
                        # 'phone': row.get('phone'),
                    }
                )

                if created:
                    self.stdout.write(self.style.SUCCESS(f"Fornecedor '{obj.name}' criado."))
                else:
                    self.stdout.write(self.style.WARNING(f"Fornecedor '{obj.name}' atualizado."))
        
        self.stdout.write(self.style.SUCCESS('Importação de Fornecedores concluída.'))