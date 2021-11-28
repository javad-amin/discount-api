from marshmallow import Schema, fields


class NewDiscountsResponseSchema(Schema):
    discoundId = fields.UUID()
