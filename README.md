How implement

```python
from simplepgconnection import PostgresqlDriver

conn_string = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
driver = PostgresqlDriver(conn_string)
```
