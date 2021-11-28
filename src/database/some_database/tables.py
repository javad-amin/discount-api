
from database.discount_dto import DiscountDto
from uuid import UUID
from datetime import datetime


claimed_discount = DiscountDto(
    discountId=UUID("3fa85f64-5717-4562-b3fc-2c963f66afa6"),
    brandId=UUID("024cc9f4-0a5e-4985-b768-69c3c52584cf"),
    validFromTime=datetime.strptime("2021-11-22 12:49:50", "%Y-%m-%d %H:%M:%S"),
    expirationTime=datetime.strptime("2022-11-28 12:49:50", "%Y-%m-%d %H:%M:%S"),
    discountName="BlackWeek2021"
)

claimed_discount.claimedBy = UUID("cda78178-b104-4b63-ae8d-aba49b800b8c")
claimed_discount.isRedeemed = True

not_claimed_discount = DiscountDto(
    discountId=UUID("8557f1ad-4c8f-4822-ab4c-c30338289574"),
    brandId=UUID("024cc9f4-0a5e-4985-b768-69c3c52584cf"),
    validFromTime=datetime.strptime("2021-11-22 12:49:50", "%Y-%m-%d %H:%M:%S"),
    expirationTime=datetime.strptime("2022-11-28 12:49:50", "%Y-%m-%d %H:%M:%S"),
    discountName="BlackWeek2021"
)


fake_discounts_table = [claimed_discount, not_claimed_discount]
