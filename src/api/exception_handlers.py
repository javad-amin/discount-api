from http import HTTPStatus

from database.database_exceptions import (
    AlreadyClaimedDatabaseException,
    AlreadyExistsDatabaseException,
    NotFoundDatabaseException
)


def handle_exceptions(app):

    @app.errorhandler(AlreadyExistsDatabaseException)
    def handle_already_exists_database_exception(e):
        return create_exception_response(HTTPStatus.BAD_REQUEST.value,
                                         str(e),
                                         HTTPStatus.BAD_REQUEST.name), HTTPStatus.BAD_REQUEST.value

    @app.errorhandler(AlreadyClaimedDatabaseException)
    def handle_already_claimed_database_exception(e):
        return create_exception_response(HTTPStatus.BAD_REQUEST.value,
                                         str(e),
                                         HTTPStatus.BAD_REQUEST.name), HTTPStatus.BAD_REQUEST.value

    @app.errorhandler(NotFoundDatabaseException)
    def handle_not_found_database_exception(e):
        return create_exception_response(HTTPStatus.NOT_FOUND.value,
                                         str(e),
                                         HTTPStatus.NOT_FOUND.name), HTTPStatus.NOT_FOUND.value

    @app.errorhandler(Exception)
    def handle_exception(e):
        return create_exception_response(HTTPStatus.INTERNAL_SERVER_ERROR.value,
                                         f"Internal server error. {str(e)}",
                                         HTTPStatus.INTERNAL_SERVER_ERROR.name), HTTPStatus.INTERNAL_SERVER_ERROR.value


def create_exception_response(status_code, message, status_name):
    return {"code": status_code, "message": message, "status": status_name}
