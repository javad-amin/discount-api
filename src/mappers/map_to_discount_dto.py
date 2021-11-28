from typing import List
from uuid import UUID
from database.discount_dto import DiscountDto
from models.request.new_discounts import NewDiscountsModel
from models.response.claimed_discount import ClaimedDiscountModel
from models.response.discount_id import DiscountIdModel


def new_discount_to_db_dto(discount_id: UUID, brandId: UUID, model: NewDiscountsModel) -> DiscountDto:
    return DiscountDto(discountId=discount_id,
                       brandId=brandId,
                       validFromTime=model.validFromTime,
                       expirationTime=model.expirationDate,
                       discountName=model.discountName)


def db_dto_to_discount_id_collection(discount_dto_collection: List[DiscountDto]) -> List[DiscountIdModel]:
    return [DiscountIdModel(str(discount.discountId)) for discount in discount_dto_collection]


def db_dto_to_claimed_discount(discount_dto: DiscountDto) -> ClaimedDiscountModel:
    return ClaimedDiscountModel(discount_dto.discountId,
                                discount_dto.claimedBy,
                                discount_dto.validFromTime,
                                discount_dto.expirationTime,
                                discount_dto.discountName)
