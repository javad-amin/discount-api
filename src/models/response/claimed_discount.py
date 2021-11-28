from dataclasses import dataclass
from uuid import UUID
from datetime import datetime


@dataclass
class ClaimedDiscountModel:
    discoundId: UUID
    claimedBy: UUID
    validFromTime: datetime
    expirationTime: datetime
    discountName: str
