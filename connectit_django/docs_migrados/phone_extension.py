# app/models/phone_extension.py
class PhoneExtension:
    def __init__(self, id=None, extension_number=None, employee_name=None, sector_id=None, unit_id=None):
        self.id = id
        self.extension_number = extension_number
        self.employee_name = employee_name
        self.sector_id = sector_id
        self.unit_id = unit_id

    def to_dict(self):
        return {
            "extensionNumber": self.extension_number,
            "employeeName": self.employee_name,
            "sectorId": self.sector_id,
            "unitId": self.unit_id
        }

    @staticmethod
    def from_dict(source, id=None):
        extension = PhoneExtension(id=id or source.get('id'), extension_number=source.get('extensionNumber'),
                                   employee_name=source.get('employeeName'), sector_id=source.get('sectorId'),
                                   unit_id=source.get('unitId'))
        return extension
