# Em: core/management/commands/import_asset_types.py

import csv
from django.core.management.base import BaseCommand
from core.models import AssetType

class Command(BaseCommand):
    help = 'Importa tipos de ativo a partir de um arquivo CSV.'

    def add_arguments(self, parser):
        parser.add_argument('csv_file_path', type=str, help='O caminho para o arquivo CSV de tipos de ativo.')

    def handle(self, *args, **options):
        csv_file_path = options['csv_file_path']
        self.stdout.write(self.style.SUCCESS(f'Iniciando a importação de Tipos de Ativo de: {csv_file_path}'))

        with open(csv_file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # update_or_create: atualiza o tipo se já existir (baseado no nome), ou cria um novo.
                # Isso torna o script seguro para ser rodado múltiplas vezes.
                asset_type, created = AssetType.objects.update_or_create(
                    name=row['name'],
                    defaults={
                        'firestore_id': row['id_firestore'],
                        'description': row.get('description', '') # Campo opcional
                    }
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f"Tipo de Ativo '{asset_type.name}' criado."))
                else:
                    self.stdout.write(self.style.WARNING(f"Tipo de Ativo '{asset_type.name}' atualizado."))

        self.stdout.write(self.style.SUCCESS('Importação de Tipos de Ativo concluída.'))