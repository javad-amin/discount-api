from flask_swagger_ui import get_swaggerui_blueprint
from flask_smorest import Api
from flask import Flask

from api.exception_handlers import handle_exceptions
from database.abc.database import IDatabase
import api.blueprint as blp
__import__('endpoints')


def create_app(database: IDatabase) -> Flask:
    """This function creates the main flask app.

    Args:
        database (IDatabase): Database layer used for CRUD operations.

    Returns:
        Flask: Returns a flask application.
    """
    app = Flask(__name__)

    swagger_ui_blp = get_swaggerui_blueprint("/swagger", "../openapi.json")

    app.config.update(
        {
            "API_TITLE": "Schedule charging API",
            "API_VERSION": "v1",
            "OPENAPI_VERSION": "3.0.3",
            "OPENAPI_URL_PREFIX": "/",
            "OPENAPI_JSON_PATH": "/openapi.json",
            "OPENAPI_SWAGGER_UI_VERSION": "3.25.0",
            "DATABASE": database,
        }
    )
    app.register_blueprint(swagger_ui_blp)

    api = Api(app)
    api.register_blueprint(blp.customers)
    api.register_blueprint(blp.brands)

    handle_exceptions(app)

    return app
