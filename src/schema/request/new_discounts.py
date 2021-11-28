from marshmallow import Schema, fields, post_load
from models.request.new_discounts import NewDiscountsModel


class NewDiscountsRequestSchema(Schema):
    discountName = fields.String(required=True)
    validFromTime = fields.DateTime()
    expirationDate = fields.DateTime()
    numberOfDiscounts = fields.Integer(required=True)

    @post_load
    def create_dto(self, data, **kwargs):
        return NewDiscountsModel(**data)
