"""
Define a classe de modelo para a entidade 'ExpenseType', que representa
os diferentes tipos de despesas que podem ser registrados e rateados no sistema.
"""

from typing import Any, Dict, Optional


class ExpenseType:
    """
    Representa um Tipo de Despesa no sistema.

    Esta classe encapsula os atributos de um tipo de despesa, fornecendo
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
        Inicializa uma nova instância de Tipo de Despesa.

        Args:
            name (str): O nome do tipo de despesa (ex: 'Telefonia', 'Aluguel de Impressora').
            description (Optional[str]): Uma descrição opcional do tipo de despesa.
            id (Optional[str]): O ID único do tipo de despesa. Será None para novos
                                tipos de despesa antes de serem salvos no Firestore.
        """
        self.id = id
        self.name = name
        self.description = description

    def to_dict(self) -> Dict[str, Any]:
        """
        Converte o objeto ExpenseType para um dicionário, adequado para ser salvo no Firestore.

        Retorna:
            Dict[str, Any]: Um dicionário representando o tipo de despesa.
                            Campos com valor `None` não serão incluídos,
                            otimizando o armazenamento no Firestore.
        """
        expense_type_dict: Dict[str, Any] = {
            "name": self.name,
            "description": self.description,
            # 'id' não é incluído aqui, pois ele é o ID do documento no Firestore
        }
        # Filtra campos com valor None para não serem salvos no Firestore
        return {k: v for k, v in expense_type_dict.items() if v is not None}

    @staticmethod
    def from_dict(source: Dict[str, Any], id: Optional[str] = None) -> "ExpenseType":
        """
        Cria um objeto ExpenseType a partir de um dicionário (geralmente vindo do Firestore).

        Args:
            source (Dict[str, Any]): O dicionário de dados a partir do qual criar o ExpenseType.
                                     Deve conter a chave 'name' e opcionalmente 'description'.
            id (Optional[str]): O ID do documento no Firestore. Se fornecido,
                                tem precedência sobre o 'id' que possa estar no 'source'.

        Retorna:
            ExpenseType: Uma nova instância da classe ExpenseType populada com os dados.
        """
        # Prioriza o 'id' passado como argumento, senão tenta pegar do source,
        # senão fica None.
        final_id: Optional[str] = id if id is not None else source.get('id')

        # Acessa os valores do dicionário de forma segura com .get()
        return ExpenseType(
            id=final_id,
            name=source.get('name', ''),  # Garante que 'name' seja uma string, mesmo se ausente
            description=source.get('description')
        )