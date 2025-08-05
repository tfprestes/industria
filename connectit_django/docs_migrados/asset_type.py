# app/models/asset_type.py

"""
Define a classe de modelo para a entidade 'AssetType', que representa
os diferentes tipos de ativos e suas características gerais no sistema.
"""

from typing import Any, Dict, Optional


class AssetType:
    """
    Representa um Tipo de Ativo no sistema.

    Esta classe encapsula os atributos gerais de um tipo de ativo, como nome,
    descrição e, opcionalmente, um Sistema Operacional padrão.
    """

    def __init__(
        self,
        name: str,
        description: Optional[str] = None,
        default_operating_system: Optional[str] = None,  # NOVO CAMPO
        id: Optional[str] = None,
    ):
        """
        Inicializa uma nova instância de Tipo de Ativo.

        Args:
            name (str): O nome do tipo de ativo (ex: 'Notebook').
            description (Optional[str]): Uma descrição opcional.
            default_operating_system (Optional[str]): O SO padrão para este tipo.
            id (Optional[str]): O ID único do tipo de ativo.
        """
        self.id = id
        self.name = name
        self.description = description
        self.defaultOperatingSystem = default_operating_system  # NOVO ATRIBUTO

    def to_dict(self) -> Dict[str, Any]:
        """
        Converte o objeto AssetType para um dicionário, adequado para o Firestore.

        Returns:
            Dict[str, Any]: Um dicionário representando o tipo de ativo,
                            com campos camelCase e sem valores None.
        """
        asset_type_dict: Dict[str, Any] = {
            "name": self.name,
            "description": self.description,
            "defaultOperatingSystem": self.defaultOperatingSystem,  # NOVO CAMPO
        }
        return {k: v for k, v in asset_type_dict.items() if v is not None}

    @staticmethod
    def from_dict(source: Dict[str, Any], id: Optional[str] = None) -> "AssetType":
        """
        Cria um objeto AssetType a partir de um dicionário do Firestore.

        Args:
            source (Dict[str, Any]): O dicionário de dados.
            id (Optional[str]): O ID do documento no Firestore.

        Returns:
            AssetType: Uma nova instância da classe AssetType.
        """
        return AssetType(
            id=id if id is not None else source.get('id'),
            name=source.get('name', ''),
            description=source.get('description'),
            default_operating_system=source.get('defaultOperatingSystem')  # NOVO CAMPO
        )