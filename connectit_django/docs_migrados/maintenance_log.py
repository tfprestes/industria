# app/models/maintenance_log.py
import datetime

class MaintenanceLog:
    """Representa um registo de manutenção no sistema."""

    def __init__(self, entity_id, entity_type, log_date, description, 
                 repair_type, cost=0.0, technician=None, parts_used=None, 
                 attachments=None, id=None):
        """
        Construtor da classe MaintenanceLog, atualizado para 'Etapa B' e 'Fase 9'.
        """
        self.id = id
        self.entity_id = entity_id              # ID do Ativo ou Equipamento de Rede
        self.entity_type = entity_type          # String: 'assets' ou 'networkEquipment'
        self.log_date = log_date                # Objeto datetime
        self.description = description
        self.repair_type = repair_type
        self.cost = float(cost) if cost is not None else 0.0
        self.technician = technician
        # 'parts_used' é agora uma lista de objetos (ex: [{'itemId': '...', 'quantityUsed': 1}])
        self.parts_used = parts_used if parts_used is not None else []
        # 'attachments' é a nova lista para os ficheiros de upload
        self.attachments = attachments if attachments is not None else []

    def to_dict(self):
        """
        Converte o objeto para um dicionário para ser salvo no Firestore.
        """
        return {
            "entityId": self.entity_id,
            "entityType": self.entity_type,
            "logDate": self.log_date,
            "description": self.description,
            "repairType": self.repair_type,
            "cost": self.cost,
            "technician": self.technician,
            "partsUsed": self.parts_used,
            "attachments": self.attachments
        }

    @staticmethod
    def from_dict(source, id=None):
        """
        Cria um objeto MaintenanceLog a partir de um dicionário vindo do Firestore.
        """
        return MaintenanceLog(
            id=id,
            entity_id=source.get('entityId'),
            entity_type=source.get('entityType'),
            log_date=source.get('logDate'),
            description=source.get('description'),
            repair_type=source.get('repairType'),
            cost=source.get('cost'),
            technician=source.get('technician'),
            # Garante que, se os campos não existirem, são criados como listas vazias
            parts_used=source.get('partsUsed', []),
            attachments=source.get('attachments', [])
        )