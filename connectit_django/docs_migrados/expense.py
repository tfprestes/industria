"""
Define a classe de modelo para a entidade 'Expense', que representa
as despesas registradas no sistema.
"""

import datetime
from typing import Any, Dict, Optional, Union


class Expense:
    """
    Representa uma Despesa no sistema.

    Esta classe encapsula os atributos de uma despesa, fornecendo
    métodos para converter o objeto para e de um dicionário, facilitando
    a interação com o Firestore. Inclui campos para valor, período de referência,
    e associações a tipos de despesa, setores, unidades e centros de custo.
    """

    def __init__(
        self,
        value: Union[float, int],  # Pode vir como int do formulário ou float do DB
        reference_month: int,
        reference_year: int,
        expense_type_id: str,  # Novo nome para o campo que armazena o ID do ExpenseType
        id: Optional[str] = None,
        sector_id: Optional[str] = None,
        unit_id: Optional[str] = None,
        cost_center_id: Optional[str] = None,
        description: Optional[str] = None,
    ):
        """
        Inicializa uma nova instância de Despesa.

        Args:
            value (Union[float, int]): O valor da despesa.
            reference_month (int): O mês de referência da despesa (1-12).
            reference_year (int): O ano de referência da despesa.
            expense_type_id (str): O ID do tipo de despesa associado.
            id (Optional[str]): O ID único da despesa. Será None para novas
                                despesas antes de serem salvas no Firestore.
            sector_id (Optional[str]): O ID do setor ao qual a despesa está associada.
            unit_id (Optional[str]): O ID da unidade ao qual a despesa está associada.
            cost_center_id (Optional[str]): O ID do centro de custo ao qual a despesa está associada.
            description (Optional[str]): Uma descrição opcional da despesa.
        """
        self.id = id
        # Garante que o valor é um float
        self.value = float(value)
        self.referenceMonth = reference_month
        self.referenceYear = reference_year
        self.expenseTypeId = expense_type_id  # Atributo renomeado
        self.sectorId = sector_id
        self.unitId = unit_id
        self.costCenterId = cost_center_id
        self.description = description

    def to_dict(self) -> Dict[str, Any]:
        """
        Converte o objeto Expense para um dicionário, adequado para ser salvo no Firestore.

        Retorna:
            Dict[str, Any]: Um dicionário representando a despesa, com campos em camelCase.
                            Campos com valor `None` não serão incluídos.
        """
        expense_dict: Dict[str, Any] = {
            "value": self.value,
            "referenceMonth": self.referenceMonth,
            "referenceYear": self.referenceYear,
            "expenseTypeId": self.expenseTypeId,  # Renomeado no dicionário
            "sectorId": self.sectorId,
            "unitId": self.unitId,
            "costCenterId": self.costCenterId,
            "description": self.description,
            # 'id' não é incluído aqui, pois ele é o ID do documento no Firestore
        }
        # Filtra campos com valor None para não serem salvos no Firestore
        return {k: v for k, v in expense_dict.items() if v is not None}

    @staticmethod
    def from_dict(source: Dict[str, Any], id: Optional[str] = None) -> "Expense":
        """
        Cria um objeto Expense a partir de um dicionário (geralmente vindo do Firestore).

        Args:
            source (Dict[str, Any]): O dicionário de dados a partir do qual criar a Despesa.
            id (Optional[str]): O ID do documento no Firestore. Se fornecido,
                                tem precedência sobre o 'id' que possa estar no 'source'.

        Retorna:
            Expense: Uma nova instância da classe Expense populada com os dados.
        """
        final_id: Optional[str] = id if id is not None else source.get('id')

        # Acessa os valores do dicionário de forma segura com .get()
        return Expense(
            id=final_id,
            value=source.get('value', 0.0),  # Default para float/int
            reference_month=source.get('referenceMonth', 1),
            reference_year=source.get('referenceYear', datetime.datetime.now().year),
            expense_type_id=source.get('expenseTypeId', ''),  # Use o novo nome do campo
            sector_id=source.get('sectorId'),
            unit_id=source.get('unitId'),
            cost_center_id=source.get('costCenterId'),
            description=source.get('description')
        )