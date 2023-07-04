import pandas as pd
from pandas import DataFrame

from interfaces.driver_interface import IDriver
from infraestructure.connection import Connection

class PostgresDriver(IDriver):
    def __init__(self, conn: str):
        self.connection = Connection(conn)

    def query(self, query: str) -> DataFrame:
        return pd.read_sql_query(query, con=self.connection)

    def execute(self, query: str) -> list[dict]:
        try:
            result = self.connection.execute(query)
            data = [dict((key, value) for key, value in row.items())
                    for row in result]
            return data
        except Exception as e:
            raise Exception(e)

    def executeWithOutRows(self, query: str) -> bool:
        try:
            self.connection.execute(query)
            return True
        except Exception as E:
            return False
        
__all__ = ['PostgresDriver']
