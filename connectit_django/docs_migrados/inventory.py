# app/models/inventory.py
class InventoryItem:
    def __init__(self, id=None, item_name=None, item_type=None, quantity=None, unit_of_measure=None, min_stock_level=None, supplier_id=None, location_description=None, last_restock_date=None):
        self.id = id
        self.item_name = item_name
        self.item_type = item_type
        self.quantity = quantity
        self.unit_of_measure = unit_of_measure
        self.min_stock_level = min_stock_level
        self.supplier_id = supplier_id
        self.location_description = location_description
        self.last_restock_date = last_restock_date

    def to_dict(self):
        return {
            "itemName": self.item_name,
            "itemType": self.item_type,
            "quantity": self.quantity,
            "unitOfMeasure": self.unit_of_measure,
            "minStockLevel": self.min_stock_level,
            "supplierId": self.supplier_id,
            "locationDescription": self.location_description,
            "lastRestockDate": self.last_restock_date
        }

    @staticmethod
    def from_dict(source, id=None):
        item = InventoryItem(id=id or source.get('id'), item_name=source.get('itemName'), item_type=source.get('itemType'),
                             quantity=source.get('quantity'), unit_of_measure=source.get('unitOfMeasure'),
                             min_stock_level=source.get('minStockLevel'), supplier_id=source.get('supplierId'),
                             location_description=source.get('locationDescription'), last_restock_date=source.get('lastRestockDate'))
        return item
