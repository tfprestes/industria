# Em: core/management/commands/import_cost_centers.py

import csv
from django.core.management.base import BaseCommand
from core.models import CostCenter

class Command(BaseCommand):
    help = 'Importa centros de custo a partir de um arquivo CSV, lidando com dados inconsistentes.'

    def add_arguments(self, parser):
        parser.add_argument('csv_file_path', type=str)

    def handle(self, *args, **options):
        csv_file_path = options['csv_file_path']
        self.stdout.write(f"Importando Centros de Custo de: {csv_file_path}")
        
        with open(csv_file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                name_and_code = row.get('name')
                firestore_id = row.get('id_firestore')

                if not name_and_code:
                    self.stdout.write(self.style.WARNING(f"Linha ignorada: nome do centro de custo em falta."))
                    continue

                # CORREÇÃO FINAL: Usamos o 'code' como a chave de negócio para encontrar o objeto.
                # Se múltiplas linhas no CSV tiverem o mesmo código, elas serão fundidas num único registo no Django.
                obj, created = CostCenter.objects.update_or_create(
                    code=name_and_code,
                    defaults={
                        'name': name_and_code,
                        'firestore_id': firestore_id  # Atualiza o firestore_id para o do último registo encontrado
                    }
                )
                
                if created:
                    self.stdout.write(self.style.SUCCESS(f"Centro de Custo '{obj.name}' criado."))
                else:
                    self.stdout.write(self.style.WARNING(f"Centro de Custo '{obj.name}' encontrado e atualizado."))
        
        self.stdout.write(self.style.SUCCESS('Importação de Centros de Custo concluída.'))