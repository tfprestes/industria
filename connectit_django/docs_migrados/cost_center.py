"""
Define a classe de modelo para a entidade 'CostCenter', que representa
os centros de custo da empresa no sistema.
"""

from typing import Any, Dict, Optional


class CostCenter:
    """
    Representa um Centro de Custo no sistema.

    Esta classe encapsula os atributos de um centro de custo, fornecendo
    métodos para converter o objeto para e de um dicionário, facilitando
    a interação com o Firestore.
    """

    def __init__(
        self,
        name: str,
        description: Optional[str] = None,
        id: Optional[str] = None,
    ):
        """
        Inicializa uma nova instância de Centro de Custo.

        Args:
            name (str): O nome do centro de custo (obrigatório).
            description (Optional[str]): Uma descrição opcional do centro de custo.
            id (Optional[str]): O ID único do centro de custo. Será None para novos
                                centros de custo antes de serem salvos no Firestore.
        """
        self.id = id
        self.name = name
        self.description = description

    def to_dict(self) -> Dict[str, Any]:
        """
        Converte o objeto CostCenter para um dicionário, adequado para ser salvo no Firestore.

        Retorna:
            Dict[str, Any]: Um dicionário representando o centro de custo.
                            Campos com valor `None` não serão incluídos,
                            otimizando o armazenamento no Firestore.
        """
        cost_center_dict: Dict[str, Any] = {
            "name": self.name,
            "description": self.description,
            # Não incluir 'id' ao salvar, pois ele é o ID do documento no Firestore
        }
        # Filtra campos com valor None para não serem salvos no Firestore
        return {k: v for k, v in cost_center_dict.items() if v is not None}

    @staticmethod
    def from_dict(source: Dict[str, Any], id: Optional[str] = None) -> "CostCenter":
        """
        Cria um objeto CostCenter a partir de um dicionário (geralmente vindo do Firestore).

        Args:
            source (Dict[str, Any]): O dicionário de dados a partir do qual criar o CostCenter.
                                     Deve conter as chaves 'name' e 'description'.
            id (Optional[str]): O ID do documento no Firestore. Se fornecido,
                                tem precedência sobre o 'id' que possa estar no 'source'.

        Retorna:
            CostCenter: Uma nova instância da classe CostCenter populada com os dados.
        """
        # Prioriza o 'id' passado como argumento, senão tenta pegar do source,
        # senão fica None (para casos onde o ID do documento é o id no objeto).
        final_id: Optional[str] = id if id is not None else source.get('id')

        # Acessa os valores do dicionário de forma segura com .get()
        return CostCenter(
            id=final_id,
            name=source.get('name', ''),  # Garante que 'name' seja uma string, mesmo se ausente
            description=source.get('description')
        )