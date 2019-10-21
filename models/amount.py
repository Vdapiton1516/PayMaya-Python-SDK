import json
from decimal import Decimal


class Amount:
    total: Decimal
    currency_code: str

    def __init__(self, *, total: Decimal = 0.0, currency_code: str = 'PHP'):
        self.total = total
        self.currency_code = currency_code

    def as_dict(self):
        data = {
            'total': str(self.total),
            'code': self.currency_code
        }

        return data

    def serialize(self):
        return json.dumps(self.as_dict())