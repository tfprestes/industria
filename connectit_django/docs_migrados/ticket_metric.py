# app/models/ticket_metric.py

import datetime

class TicketMetric:
    def __init__(self, reference_month, reference_year, sector_id, unit_id, cost_center_id, count, notes='', id=None):
        self.id = id
        self.reference_month = int(reference_month)
        self.reference_year = int(reference_year)
        self.sector_id = sector_id
        self.unit_id = unit_id
        self.cost_center_id = cost_center_id
        self.count = int(count)
        self.notes = notes
        # Timestamps de controle
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """Converte o objeto para um dicionário para salvar no Firestore."""
        metric_dict = {
            'referenceMonth': self.reference_month,
            'referenceYear': self.reference_year,
            'sectorId': self.sector_id,
            'unitId': self.unit_id,
            'costCenterId': self.cost_center_id,
            'count': self.count,
            'notes': self.notes,
            'createdAt': self.created_at,
            'updatedAt': self.updated_at
        }
        return metric_dict

    @staticmethod
    def from_dict(source, id=None):
        """Cria um objeto TicketMetric a partir de um dicionário do Firestore."""
        return TicketMetric(
            reference_month=source.get('referenceMonth'),
            reference_year=source.get('referenceYear'),
            sector_id=source.get('sectorId'),
            unit_id=source.get('unitId'),
            cost_center_id=source.get('costCenterId'),
            count=source.get('count'),
            notes=source.get('notes', ''),
            id=id
        )