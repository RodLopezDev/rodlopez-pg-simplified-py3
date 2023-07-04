from pandas import DataFrame


class IDriver:
    def query(self, query: str) -> DataFrame:  # type: ignore
        pass

    def execute(self, query: str) -> list[dict]:  # type: ignore
        pass

    def executeWithOutRows(self, query: str) -> bool:  # type: ignore
        pass


__all__ = ["IDriver"]
