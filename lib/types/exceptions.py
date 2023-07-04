class PostgresqlException(Exception):
    def __init__(self, message=None):
        if message:
            self.message = message
        else:
            self.message = 'PostgreSQL exception, check config or query'


class DataNotFoundException(Exception):
    def __init__(self, message=None):
        if message:
            self.message = message
        else:
            self.message = 'Data not found'