# Em: contracts/management/commands/import_contract_types.py

import csv
from django.core.management.base import BaseCommand
from contracts.models import ContractType

class Command(BaseCommand):
    help = 'Extrai e cria tipos de contrato a partir de um arquivo CSV de contratos.'

    def add_arguments(self, parser):
        parser.add_argument('csv_file_path', type=str)

    def handle(self, *args, **options):
        csv_file_path = options['csv_file_path']
        self.stdout.write("Extraindo tipos de contrato...")
        
        contract_types = set()
        with open(csv_file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                category_name = row.get('category')
                if category_name:
                    contract_types.add(category_name.strip())
        
        for type_name in sorted(list(contract_types)):
            obj, created = ContractType.objects.get_or_create(name=type_name)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Tipo de Contrato '{type_name}' criado."))
        
        self.stdout.write(self.style.SUCCESS('Criação de Tipos de Contrato concluída.'))