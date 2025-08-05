# app/models/extension.py

class Extension:
    """Representa um ramal telefónico no sistema."""

    def __init__(self, number, user_name, sector_id, unit_id, notes=None, id=None):
        self.id = id
        self.number = number
        self.user_name = user_name
        self.sector_id = sector_id
        self.unit_id = unit_id # <-- Campo adicionado
        self.notes = notes if notes is not None else ""

    def to_dict(self):
        """Converte o objeto para um dicionário para salvar no Firestore."""
        return {
            'number': self.number,
            'userName': self.user_name,
            'sectorId': self.sector_id,
            'unitId': self.unit_id, # <-- Campo adicionado
            'notes': self.notes
        }

    @staticmethod
    def from_dict(source, id=None):
        """Cria um objeto Extension a partir de um dicionário do Firestore."""
        return Extension(
            id=id,
            number=source.get('number'),
            user_name=source.get('userName'),
            sector_id=source.get('sectorId'),
            unit_id=source.get('unitId'), # <-- Campo adicionado
            notes=source.get('notes')
        )