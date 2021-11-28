from marshmallow import Schema, fields


class ClaimedDiscountResponseSchema(Schema):
    discoundId = fields.UUID(required=True)
    claimedBy = fields.UUID(required=True)
    validFromTime = fields.DateTime()
    expirationTime = fields.DateTime()
    discountName = fields.String()
