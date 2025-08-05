# app/models/sector.py
class Sector:
    def __init__(self, id=None, name=None, description=None, associated_cost_center_id=None):
        self.id = id
        self.name = name
        self.description = description
        self.associated_cost_center_id = associated_cost_center_id # Novo campo

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "associatedCostCenterId": self.associated_cost_center_id
        }

    @staticmethod
    def from_dict(source, id=None):
        sector = Sector(id=id or source.get('id'),
                       name=source.get('name'),
                       description=source.get('description'),
                       associated_cost_center_id=source.get('associatedCostCenterId'))
        return sector
