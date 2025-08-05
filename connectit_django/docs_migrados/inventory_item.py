# app/models/inventory_item.py

class InventoryItem:
    """Representa um item no estoque da empresa."""

    def __init__(self, item_name, item_type, quantity, unit_of_measure, 
                 min_stock_level=0, supplier_id=None, location_description=None, id=None):
        self.id = id
        self.item_name = item_name
        self.item_type = item_type
        self.quantity = int(quantity)
        self.unit_of_measure = unit_of_measure
        self.min_stock_level = int(min_stock_level)
        self.supplier_id = supplier_id
        self.location_description = location_description

    def to_dict(self):
        """Converte o objeto para um dicionário para salvar no Firestore."""
        return {
            'itemName': self.item_name,
            'itemType': self.item_type,
            'quantity': self.quantity,
            'unitOfMeasure': self.unit_of_measure,
            'minStockLevel': self.min_stock_level,
            'supplierId': self.supplier_id,
            'locationDescription': self.location_description
        }

    @staticmethod
    def from_dict(source, id=None):
        """Cria um objeto InventoryItem a partir de um dicionário do Firestore."""
        return InventoryItem(
            id=id,
            item_name=source.get('itemName'),
            item_type=source.get('itemType'),
            quantity=source.get('quantity'),
            unit_of_measure=source.get('unitOfMeasure'),
            min_stock_level=source.get('minStockLevel', 0),
            supplier_id=source.get('supplierId'),
            location_description=source.get('locationDescription')
        )