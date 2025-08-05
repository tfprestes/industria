# app/models/network_equipment.py

"""
Define os modelos de dados para a gestão de Equipamentos de Rede.
"""

from dataclasses import asdict, dataclass
from typing import Any, Dict, List, Optional


@dataclass
class Port:
    """
    Representa uma única porta de um equipamento de rede (como um switch).

    Attributes:
        number (int): O número da porta.
        status (str): O estado da porta (ex: 'Ativa', 'Inativa', 'Manutenção').
        vlan (str): A VLAN associada a esta porta.
        description (str): Uma descrição para a utilização da porta.
        connected_mac (Optional[str]): O endereço MAC do dispositivo conectado.
        speed (Optional[str]): A velocidade negociada da porta (ex: '1G', '100M').
        poe_status (bool): O estado do Power over Ethernet (Ligado/Desligado).
    """
    number: int
    status: str = 'Ativa'
    vlan: str = ''
    description: str = ''
    connected_mac: Optional[str] = None
    speed: Optional[str] = '1G'
    poe_status: bool = False


class NetworkEquipment:
    """Representa um equipamento de infraestrutura de rede no sistema."""

    def __init__(self, equipment_type: str, brand: str, model: str,
                 ip_address: Optional[str] = None, firmware_version: Optional[str] = None,
                 sector_id: Optional[str] = None, location_description: Optional[str] = None, 
                 network_category: Optional[str] = None,
                 ports: Optional[List[Port]] = None, 
                 attachments: Optional[List[Dict[str, Any]]] = None, 
                 id: Optional[str] = None):
        """Construtor da classe NetworkEquipment."""
        self.id = id
        self.type = equipment_type
        self.brand = brand
        self.model = model
        self.ipAddress = ip_address
        self.firmwareVersion = firmware_version
        self.assignedSectorId = sector_id
        self.locationDescription = location_description
        self.networkCategory = network_category
        self.ports = sorted(ports, key=lambda p: p.number) if ports is not None else []
        self.attachments = attachments if attachments is not None else []

    def to_dict(self) -> Dict[str, Any]:
        """Converte o objeto para um dicionário para ser salvo no Firestore."""
        data = {
            "type": self.type,
            "brand": self.brand,
            "model": self.model,
            "ipAddress": self.ipAddress,
            "firmwareVersion": self.firmwareVersion,
            "assignedSectorId": self.assignedSectorId,
            "locationDescription": self.locationDescription,
            "networkCategory": self.networkCategory,
            "ports": [asdict(port) for port in self.ports],
            "attachments": self.attachments
        }
        return {k: v for k, v in data.items() if v is not None}

    @staticmethod
    def from_dict(source: Dict[str, Any], doc_id: str) -> 'NetworkEquipment':
        """Cria um objeto NetworkEquipment a partir de um dicionário do Firestore."""
        ports_data = source.get('ports', [])
        ports_list = [Port(**port_data) for port_data in ports_data]
        
        return NetworkEquipment(
            id=doc_id,
            equipment_type=source.get('type'),
            brand=source.get('brand'),
            model=source.get('model'),
            ip_address=source.get('ipAddress'),
            firmware_version=source.get('firmwareVersion'),
            sector_id=source.get('assignedSectorId'),
            location_description=source.get('locationDescription'),
            network_category=source.get('networkCategory'),
            ports=ports_list,
            attachments=source.get('attachments', [])
        )