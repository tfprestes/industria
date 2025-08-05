# app/models/asset.py

"""
Define a classe de modelo para a entidade 'Asset', que representa
os ativos da empresa, como computadores, licenças, etc., no sistema.
"""

import datetime
from typing import Any, Dict, List, Optional


class Asset:
    """
    Representa um ativo físico ou lógico no sistema de gestão de ativos.

    Esta classe encapsula todos os atributos de um ativo, fornecendo métodos
    para converter o objeto para e de um dicionário, facilitando a
    interação com o Firestore.
    """

    def __init__(
        self,
        # --- Campos Obrigatórios ---
        asset_type_id: str,
        brand: str,
        model: str,
        status: str,
        assigned_sector_id: str,
        assigned_unit_id: str,
        assigned_cost_center_id: str,
        lease_value: float,
        lease_date: Optional[datetime.datetime],

        # --- Campos Opcionais ---
        id: Optional[str] = None,
        serial_number: Optional[str] = None,
        internal_tag: Optional[str] = None,
        user: Optional[str] = None,
        responsible: Optional[str] = None,
        description: Optional[str] = None,
        supplier_id: Optional[str] = None,
        invoice_number: Optional[str] = None,
        contract_duration_months: Optional[int] = None,
        
        # --- Datas Opcionais ---
        receipt_date: Optional[datetime.datetime] = None,
        invoice_date: Optional[datetime.datetime] = None,
        delivery_activation_date: Optional[datetime.datetime] = None,
        contract_end_date: Optional[datetime.datetime] = None,
        deactivation_date: Optional[datetime.datetime] = None,
        exclusion_date: Optional[datetime.datetime] = None,
        
        # --- Especificações Técnicas ---
        operating_system: Optional[str] = None,
        processor: Optional[str] = None,
        memory: Optional[str] = None,
        office_version: Optional[str] = None,
        ip_address: Optional[str] = None,  # <-- NOVO CAMPO ADICIONADO
        
        # --- Campos de Celular ---
        imei: Optional[str] = None,
        phone_number: Optional[str] = None,
        
        # --- Listas ---
        shared_with: Optional[List[Dict[str, Any]]] = None,
        attachments: Optional[List[Dict[str, Any]]] = None
    ):
        """Inicializa uma nova instância de Ativo."""
        self.id = id
        self.assetTypeId = asset_type_id
        self.brand = brand
        self.model = model
        self.status = status
        self.serialNumber = serial_number
        self.internalTag = internal_tag
        self.user = user
        self.responsible = responsible
        self.description = description
        self.assignedSectorId = assigned_sector_id
        self.assignedUnitId = assigned_unit_id
        self.assignedCostCenterId = assigned_cost_center_id
        self.leaseValue = lease_value
        self.leaseDate = lease_date
        self.receiptDate = receipt_date
        self.invoiceNumber = invoice_number
        self.invoiceDate = invoice_date
        self.supplierId = supplier_id
        self.contractDurationMonths = contract_duration_months
        self.contractEndDate = contract_end_date
        self.deliveryActivationDate = delivery_activation_date
        self.deactivationDate = deactivation_date
        self.exclusionDate = exclusion_date
        self.operatingSystem = operating_system
        self.processor = processor
        self.memory = memory
        self.officeVersion = office_version
        self.ipAddress = ip_address # <-- NOVO ATRIBUTO
        self.imei = imei
        self.phoneNumber = phone_number
        self.sharedWith = shared_with if shared_with is not None else []
        self.attachments = attachments if attachments is not None else []

    def to_dict(self) -> Dict[str, Any]:
        """Converte o objeto Asset para um dicionário, removendo valores nulos ou vazios."""
        asset_dict = self.__dict__.copy()
        asset_dict.pop('id', None)
        return {k: v for k, v in asset_dict.items() if v is not None and v != ''}

    @staticmethod
    def from_dict(source: Dict[str, Any], id: str) -> "Asset":
        """Cria um objeto Asset a partir de um dicionário do Firestore."""
        # O construtor já lida com valores ausentes definindo-os como None
        # Usar **source passa todos os campos do dicionário como argumentos
        return Asset(id=id, **source)