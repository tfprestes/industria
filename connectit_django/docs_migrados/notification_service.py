# app/services/notification_service.py
# Lógica para envio de notificações (e-mail, alertas no sistema)

def send_contract_alert_notification(contract_details):
    """Envia uma notificação sobre contrato próximo do vencimento."""
    print(f"Alerta de contrato para: {contract_details.get('assetName', 'Ativo Desconhecido')} - Vence em: {contract_details.get('contractEndDate')}")

def send_low_stock_notification(item_details):
    """Envia uma notificação sobre item com estoque baixo."""
    print(f"Alerta de estoque baixo para: {item_details.get('itemName')} - Quantidade atual: {item_details.get('quantity')}")
