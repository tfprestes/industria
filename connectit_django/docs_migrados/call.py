# app/models/call.py
class Call:
    def __init__(self, id=None, title=None, description=None, open_date=None, status=None, resolution_date=None, sector_id=None, unit_id=None, cost_center_id=None, reference_month=None, reference_year=None, attachments=None):
        self.id = id
        self.title = title
        self.description = description
        self.open_date = open_date
        self.status = status
        self.resolution_date = resolution_date
        self.sector_id = sector_id
        self.unit_id = unit_id
        self.cost_center_id = cost_center_id
        self.reference_month = reference_month
        self.reference_year = reference_year
        self.attachments = attachments or [] # List of dicts: {fileName, fileUrl, uploadDate, uploadedBy}

    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "openDate": self.open_date,
            "status": self.status,
            "resolutionDate": self.resolution_date,
            "sectorId": self.sector_id,
            "unitId": self.unit_id,
            "costCenterId": self.cost_center_id,
            "referenceMonth": self.reference_month,
            "referenceYear": self.reference_year,
            "attachments": self.attachments
        }

    @staticmethod
    def from_dict(source, id=None):
        call = Call(id=id or source.get('id'), title=source.get('title'), description=source.get('description'),
                    open_date=source.get('openDate'), status=source.get('status'),
                    resolution_date=source.get('resolutionDate'), sector_id=source.get('sectorId'),
                    unit_id=source.get('unitId'), cost_center_id=source.get('costCenterId'),
                    reference_month=source.get('referenceMonth'), reference_year=source.get('referenceYear'),
                    attachments=source.get('attachments'))
        return call
