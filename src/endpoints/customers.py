from dataclasses import asdict
from flask.views import MethodView
from uuid import UUID

from api.blueprint import customers as blp
from database.discount_dto import UpdateDiscountDto
from mappers.map_to_discount_dto import db_dto_to_claimed_discount
from schema.response.claimed_discount import ClaimedDiscountResponseSchema
from flask import current_app


@blp.route("/<uuid:customerId>/discounts/<uuid:discountId>")
class PetsById(MethodView):
    @blp.response(200, ClaimedDiscountResponseSchema)
    def put(self, customerId: UUID, discountId: UUID) -> dict:
        """Claim a discount for a customer.
        ---
        Args:
            customerId (dict): Unique Id for a customer.
            discountId (UUID): Unique Id for a discount.

        Returns:
            dict: Response of the request as python dict.
        """
        db = current_app.config['DATABASE']
        database_response = db.update_discount(UpdateDiscountDto(discountId, customerId))
        claimed_discount = db_dto_to_claimed_discount(database_response)
        return asdict(claimed_discount)
