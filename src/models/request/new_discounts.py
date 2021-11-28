from dataclasses import dataclass
from datetime import datetime


@dataclass
class NewDiscountsModel:
    discountName: str
    validFromTime: datetime
    expirationDate: datetime
    numberOfDiscounts: int
