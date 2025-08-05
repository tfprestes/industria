# Em: core/management/commands/import_assets.py

import csv
from datetime import datetime
from django.core.management.base import BaseCommand
from django.db import IntegrityError
from core.models import Asset, AssetType, Supplier, Unit, Sector, CostCenter

class Command(BaseCommand):
    help = 'Importa ativos de um CSV, lidando de forma robusta com relacionamentos em falta e dados sujos.'

    def add_arguments(self, parser):
        parser.add_argument('csv_file_path', type=str, help='O caminho para o arquivo CSV de ativos.')

    def handle(self, *args, **options):
        csv_file_path = options['csv_file_path']
        self.stdout.write(self.style.SUCCESS(f'Iniciando a importação de Ativos de: {csv_file_path}'))

        with open(csv_file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            
            for i, row in enumerate(reader, 1):
                firestore_id = row.get('id_firestore')
                if not firestore_id:
                    self.stdout.write(self.style.WARNING(f"Linha {i} ignorada: firestore_id em falta."))
                    continue
                
                try:
                    # --- Lógica de busca de relacionamentos mais robusta ---
                    def get_related(model, fs_id):
                        if not fs_id or fs_id == 'null': return None
                        try:
                            return model.objects.get(firestore_id=fs_id)
                        except model.DoesNotExist:
                            self.stdout.write(self.style.WARNING(f"AVISO (Linha {i}): {model.__name__} com firestore_id '{fs_id}' não encontrado. O campo ficará nulo."))
                            return None

                    asset_type = get_related(AssetType, row.get('assetTypeId'))
                    supplier = get_related(Supplier, row.get('supplierId'))
                    unit = get_related(Unit, row.get('assignedUnitId'))
                    sector = get_related(Sector, row.get('assignedSectorId'))
                    cost_center = get_related(CostCenter, row.get('assignedCostCenterId'))

                    # Validação Mínima: Um ativo precisa ter pelo menos Tipo e Unidade
                    if not asset_type or not unit:
                        self.stderr.write(self.style.ERROR(f"ERRO CRÍTICO (Linha {i}): Tipo ou Unidade em falta para o ativo com firestore_id {firestore_id}. Linha ignorada."))
                        continue
                    
                    # --- Tratamento de Datas ---
                    def parse_date(date_str):
                        if not date_str: return None
                        return datetime.fromisoformat(date_str.replace('Z', '+00:00'))
                    
                    # --- Limpeza de Dados ---
                    # Garante que campos únicos vazios sejam salvos como Nulos
                    serial_number = row.get('serialNumber') if row.get('serialNumber') else None
                    internal_tag = row.get('internalTag') if row.get('internalTag') else None

                    # --- Criação ou Atualização do Ativo ---
                    asset, created = Asset.objects.update_or_create(
                        firestore_id=firestore_id,
                        defaults={
                            'brand': row.get('brand', ''), 'model': row.get('model', ''),
                            'status': row.get('status', 'em_estoque'),
                            'serial_number': serial_number, 'internal_tag': internal_tag,
                            'description': row.get('description', ''), 'user': row.get('user', ''),
                            'lease_value': float(row.get('leaseValue', 0.0)),
                            'invoice_number': row.get('invoiceNumber', ''),
                            'contract_duration_months': int(row['contractDurationMonths']) if row.get('contractDurationMonths') else None,
                            'asset_type': asset_type, 'supplier': supplier, 'assigned_unit': unit,
                            'assigned_sector': sector, 'assigned_cost_center': cost_center,
                            'receipt_date': parse_date(row.get('receiptDate')),
                            'invoice_date': parse_date(row.get('invoiceDate')),
                            'lease_date': parse_date(row.get('leaseDate')),
                            'delivery_activation_date': parse_date(row.get('deliveryActivationDate')),
                            'contract_end_date': parse_date(row.get('contractEndDate')),
                            'deactivation_date': parse_date(row.get('deactivationDate')),
                            'exclusion_date': parse_date(row.get('exclusionDate')),
                            'operating_system': row.get('operatingSystem', ''), 'processor': row.get('processor', ''),
                            'memory': row.get('memory', ''), 'office_version': row.get('officeVersion', ''),
                            'ip_address': row.get('ipAddress', ''), 'imei': row.get('imei', ''),
                            'phone_number': row.get('phoneNumber', ''),
                        }
                    )

                    if created:
                        self.stdout.write(self.style.SUCCESS(f'Linha {i}: Ativo criado - {asset}'))
                    else:
                        self.stdout.write(self.style.WARNING(f'Linha {i}: Ativo atualizado - {asset}'))

                except IntegrityError as e:
                    self.stderr.write(self.style.ERROR(f"ERRO DE INTEGRIDADE (Linha {i}): S/N ou Etiqueta duplicada para o ativo com firestore_id {firestore_id}."))
                except Exception as e:
                    self.stderr.write(self.style.ERROR(f"ERRO INESPERADO (Linha {i}): Ativo com firestore_id {firestore_id}. Detalhe: {e}"))

        self.stdout.write(self.style.SUCCESS('Importação de Ativos concluída.'))