from flask_smorest import Blueprint

customers = Blueprint(
    "Customers",
    __name__,
    url_prefix="/customers/",
    description="Customer's operations on discounts."
)

brands = Blueprint(
    "Brands",
    __name__,
    url_prefix="/brands/",
    description="Brand's operations on discounts."
)
