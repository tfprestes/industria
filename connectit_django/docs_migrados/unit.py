# app/models/unit.py
class Unit:
    def __init__(self, id=None, name=None, type=None, cnpj=None, address=None, description=None):
        self.id = id
        self.name = name
        self.type = type # 'Matriz', 'Filial'
        self.cnpj = cnpj
        self.address = address or {} # street, number, complement, neighborhood, city, state, zipCode, country
        self.description = description

    def to_dict(self):
        return {
            "name": self.name,
            "type": self.type,
            "cnpj": self.cnpj,
            "address": self.address,
            "description": self.description
        }

    @staticmethod
    def from_dict(source, id=None):
        unit = Unit(id=id or source.get('id'), name=source.get('name'), type=source.get('type'), cnpj=source.get('cnpj'), address=source.get('address'), description=source.get('description'))
        return unit
