# app/models/contract.py
import datetime
from typing import Any, Dict, Optional

class Contract:
    def __init__(self, id: Optional[str] = None, name: str = '', supplierId: str = '', 
                 category: str = '', value: float = 0.0, billingCycle: str = 'Mensal', 
                 paymentDay: int = 1, startDate: Optional[datetime.datetime] = None, 
                 endDate: Optional[datetime.datetime] = None, status: str = 'Ativo', 
                 assignedSectorId: str = '', notes: str = ''):
        self.id = id
        self.name = name
        self.supplierId = supplierId
        self.category = category
        self.value = value
        self.billingCycle = billingCycle
        self.paymentDay = paymentDay
        self.startDate = startDate
        self.endDate = endDate
        self.status = status
        self.assignedSectorId = assignedSectorId
        self.notes = notes

    def to_dict(self) -> Dict[str, Any]:
        """Converte o objeto para um dicionário para salvar no Firestore."""
        return {
            'name': self.name,
            'supplierId': self.supplierId,
            'category': self.category,
            'value': self.value,
            'billingCycle': self.billingCycle,
            'paymentDay': self.paymentDay,
            'startDate': self.startDate,
            'endDate': self.endDate,
            'status': self.status,
            'assignedSectorId': self.assignedSectorId,
            'notes': self.notes,
        }