class DatabaseException(Exception):
    def __init__(self, message):
        super().__init__(message)


class AlreadyExistsDatabaseException(DatabaseException):
    def __init__(self, message):
        super().__init__(message)


class NotFoundDatabaseException(DatabaseException):
    def __init__(self, message):
        super().__init__(message)


class AlreadyClaimedDatabaseException(DatabaseException):
    def __init__(self, message):
        super().__init__(message)
