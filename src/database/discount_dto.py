from dataclasses import dataclass, field
from uuid import UUID
from datetime import datetime


# Some of the fields bellow are not used by the two implemented endpoints, like we can imagine
# Another endpoint for redeeming the discount code if it is not expired.
@dataclass
class DiscountDto:
    discountId: UUID
    brandId: UUID
    validFromTime: datetime
    expirationTime: datetime
    discountName: str
    claimedBy: UUID = field(init=False)
    isRedeemed: bool = field(init=False)


@dataclass
class ReadDiscountDto:
    discountId: UUID


@dataclass
class UpdateDiscountDto:
    discountId: UUID
    claimedBy: UUID
    validFromTime: datetime = field(init=False)
    expirationTime: datetime = field(init=False)
    isRedeemed: bool = field(init=False)


@dataclass
class DeleteDiscountDto:
    discountId: UUID
