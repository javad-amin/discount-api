import uuid
from flask.views import MethodView
from dataclasses import asdict

from api.blueprint import brands as blp
from mappers.map_to_discount_dto import db_dto_to_discount_id_collection, new_discount_to_db_dto
from models.request.new_discounts import NewDiscountsModel
from schema.request.new_discounts import NewDiscountsRequestSchema
from schema.response.new_discounts import NewDiscountsResponseSchema
from flask import current_app


@blp.route("/<uuid:brandId>/discounts")
class Brand(MethodView):
    @blp.arguments(NewDiscountsRequestSchema)
    @blp.response(201, NewDiscountsResponseSchema(many=True))
    def post(self, body: NewDiscountsModel, brandId: uuid.UUID) -> dict:
        """Generate discount codes for a brand.
        ---
        Args:
            body (dict): The body of the request.
            brandId (UUID): Unique Id for a brand.

        Returns:
            dict: Response of the request as python dict.
        """
        db = current_app.config['DATABASE']
        discount_collection = []
        for i in range(body.numberOfDiscounts):
            discount_dto = new_discount_to_db_dto(discount_id=uuid.uuid4(),
                                                  brandId=brandId,
                                                  model=body)
            discount_collection.append(discount_dto)
        database_response = db.create_batch_discount(discount_collection)
        discount_id_collection = db_dto_to_discount_id_collection(database_response)
        return ([asdict(x) for x in discount_id_collection])
