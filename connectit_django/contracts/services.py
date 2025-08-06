# ==============================================================================
# contracts/services.py - Camada de Serviço para Lógicas de Negócio
# ==============================================================================
"""
Este arquivo contém as lógicas de negócio complexas relacionadas a contratos,
mantendo os modelos (models.py) limpos e focados em dados.
"""

from dateutil.relativedelta import relativedelta
from .models import ScheduledPayment, Contract

def generate_payments_for_contract(contract: Contract):
    """
    Apaga pagamentos existentes (se houver) e gera um novo cronograma de
    parcelas para um determinado contrato.

    Esta função deve ser chamada explicitamente após a criação ou atualização
    de um contrato que necessite de um novo cronograma.
    """
    # Limpa parcelas antigas para evitar duplicatas ao re-gerar
    contract.payments.all().delete()

    if not (contract.start_date and contract.duration_months):
        print(f"Contrato {contract.id} não possui dados suficientes para gerar parcelas.")
        return # Não faz nada se os dados necessários não estiverem presentes

    print(f"Gerando {contract.duration_months} parcelas para o Contrato {contract.id}...")

    payments_to_create = []
    for i in range(contract.duration_months):
        due_date = contract.start_date + relativedelta(months=i)
        
        # Tenta definir o dia do pagamento, ajustando para o último dia do mês se o dia não existir
        try:
            due_date = due_date.replace(day=contract.payment_day)
        except ValueError:
            # Lógica para encontrar o último dia do mês corrente
            # Vai para o dia 28, avança 4 dias (garantido de cair no próximo mês),
            # vai para o dia 1 desse mês e subtrai um dia.
            last_day_of_month = (due_date.replace(day=28) + relativedelta(days=4)).replace(day=1) - relativedelta(days=1)
            due_date = last_day_of_month

        payments_to_create.append(
            ScheduledPayment(
                contract=contract,
                due_date=due_date,
                value=contract.monthly_value,
                description=f"Parcela {i + 1} de {contract.duration_months}"
            )
        )
    
    # Cria todos os pagamentos em uma única operação de banco de dados (mais eficiente)
    ScheduledPayment.objects.bulk_create(payments_to_create)
    print("Parcelas geradas com sucesso.")