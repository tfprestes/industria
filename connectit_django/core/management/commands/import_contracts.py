# Em: contracts/management/commands/import_contracts.py

import csv
from datetime import datetime
from django.core.management.base import BaseCommand
from contracts.models import Contract, ContractType
from core.models import Supplier

class Command(BaseCommand):
    help = 'Importa contratos, reconciliando fornecedores pelo nome e criando placeholders se necessário.'

    def add_arguments(self, parser):
        parser.add_argument('csv_file_path', type=str)

    def handle(self, *args, **options):
        csv_file_path = options['csv_file_path']
        self.stdout.write(self.style.SUCCESS(f'Iniciando a importação de Contratos de: {csv_file_path}'))

        # Garante a existência de um fornecedor placeholder
        placeholder_supplier, _ = Supplier.objects.get_or_create(name="[FORNECEDOR A DEFINIR]")

        with open(csv_file_path, mode='r', encoding='utf-8-sig') as file:
            reader = csv.DictReader(file, delimiter=';')
            
            for i, row in enumerate(reader, 1):
                firestore_id = row.get('id_firestore') or row.get('\ufeffid_firestore')
                if not firestore_id:
                    self.stdout.write(self.style.WARNING(f"Linha {i} ignorada: firestore_id em falta."))
                    continue

                try:
                    # --- RECONCILIAÇÃO PELO NOME DO FORNECEDOR (COLUNA 'name') ---
                    supplier_name = row.get('name', '').strip()
                    supplier = None

                    if supplier_name:
                        supplier, created = Supplier.objects.get_or_create(name=supplier_name)
                        if created:
                            self.stdout.write(self.style.SUCCESS(f"AVISO (Linha {i}): Fornecedor '{supplier_name}' não encontrado e foi criado automaticamente."))
                    else:
                        # Se o nome do fornecedor estiver vazio no CSV, usa o placeholder
                        supplier = placeholder_supplier
                        self.stdout.write(self.style.WARNING(f"AVISO (Linha {i}): Nome do fornecedor em falta. Usando placeholder."))

                    # --- O resto da lógica continua igual ---
                    category_name = row.get('category', '').strip()
                    start_date_str = row.get('startDate')

                    if not category_name or not start_date_str:
                        self.stderr.write(self.style.ERROR(f"ERRO (Linha {i}): Categoria ou Data de Início em falta para o contrato {firestore_id}."))
                        continue
                        
                    contract_type = ContractType.objects.get(name=category_name)
                    
                    def parse_date(date_str):
                        return datetime.strptime(date_str, '%d/%m/%Y').date()

                    contract, created = Contract.objects.update_or_create(
                        firestore_id=firestore_id,
                        defaults={
                            'supplier': supplier, 'contract_type': contract_type,
                            'contract_number': row.get('contractNumber'), 'contract_object': row.get('name', ''),
                            'status': row.get('status', 'ativo').lower(), 'start_date': parse_date(start_date_str),
                            'duration_months': int(row.get('durationMonths') or 0),
                            'monthly_value': float(row.get('value').replace(',', '.') or 0.0),
                            'payment_day': int(row.get('paymentDay') or 1),
                            'observations': row.get('notes', ''),
                        }
                    )

                    if created:
                        self.stdout.write(self.style.SUCCESS(f'Linha {i}: Contrato "{contract}" criado.'))
                    else:
                        self.stdout.write(self.style.WARNING(f'Linha {i}: Contrato "{contract}" atualizado.'))

                except Exception as e:
                    self.stderr.write(self.style.ERROR(f"ERRO INESPERADO (Linha {i}): Contrato {firestore_id}. Detalhe: {e}"))

        self.stdout.write(self.style.SUCCESS('Importação de Contratos concluída.'))