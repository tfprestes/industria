# Em: core/management/commands/import_sectors.py
import csv
from django.core.management.base import BaseCommand
from core.models import Sector, CostCenter

class Command(BaseCommand):
    help = 'Importa setores a partir de um arquivo CSV, lidando com nomes duplicados.'

    def add_arguments(self, parser):
        parser.add_argument('csv_file_path', type=str)

    def handle(self, *args, **options):
        csv_file_path = options['csv_file_path']
        self.stdout.write(f"Importando Setores de: {csv_file_path}")

        with open(csv_file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                sector_name = row.get('name')
                if not sector_name:
                    self.stdout.write(self.style.WARNING("Linha ignorada: nome do setor em falta."))
                    continue
                
                cost_center_firestore_id = row.get('associatedCostCenterId')
                cost_center = None
                if cost_center_firestore_id:
                    try:
                        cost_center = CostCenter.objects.get(firestore_id=cost_center_firestore_id)
                    except CostCenter.DoesNotExist:
                        self.stderr.write(self.style.ERROR(f"ERRO: Centro de Custo com firestore_id '{cost_center_firestore_id}' não encontrado para o Setor '{sector_name}'."))
                        continue
                
                # CORREÇÃO: Usamos o 'name' como a chave de negócio para encontrar o objeto.
                obj, created = Sector.objects.update_or_create(
                    name=sector_name,
                    defaults={
                        'firestore_id': row['id_firestore'],
                        'cost_center': cost_center
                    }
                )
                
                if created:
                    self.stdout.write(self.style.SUCCESS(f"Setor '{obj.name}' criado."))
                else:
                    self.stdout.write(self.style.WARNING(f"Setor '{obj.name}' encontrado e atualizado."))

        self.stdout.write(self.style.SUCCESS('Importação de Setores concluída.'))