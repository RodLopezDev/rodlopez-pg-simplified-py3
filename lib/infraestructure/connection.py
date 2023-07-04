from sqlalchemy import create_engine, engine


def Connection(conn_string: str) -> engine.Connection:
    db = create_engine(conn_string)
    conn = db.connect()
    return conn

__all__ = ['Connection']
