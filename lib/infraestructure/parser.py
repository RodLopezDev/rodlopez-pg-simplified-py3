from typing import Any
from pandas import DataFrame, Series

from types.exceptions import PostgresqlException, DataNotFoundException
from interfaces.driver_interface import IDriver

class Parser():
    def __init__(self, driver: IDriver):
        self.driver = driver

    def query(self, query: str, exceptionMessage: str, noException: bool = False) -> DataFrame:
        result = None
        try:
            dataframe = self.driver.query(query)
            result = dataframe
        except:
            raise PostgresqlException()

        if (result.size == 0):
            if (noException == True):
                return DataFrame()
            raise DataNotFoundException(exceptionMessage)
        return result

    def queryAsOne(self, query: str, exceptionMessage: str, noException: bool = False) -> Series:
        result = Series(dtype='float64')
        dataframe = self.query(query, exceptionMessage, noException)

        if (dataframe.size == 0):
            raise DataNotFoundException(exceptionMessage)

        for index, row in dataframe.iterrows():
            if (result.empty == False):
                continue
            result = row
        return result

    def execute(self, query: str, exceptionMessage: str, noException: bool = False) -> dict:
        result = self.driver.execute(query)
        if (len(result) == 0):
            if (noException == True):
                return dict()
            raise DataNotFoundException(exceptionMessage)

        return result[0]

    def executeWithOutRows(self, query: str) -> bool:
        return self.driver.executeWithOutRows(query)


__all__ = ["Parser"]
