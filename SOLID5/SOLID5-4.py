from abc import abstractmethod


class DBConnection:
    @abstractmethod
    def query(self, sql: str) -> list:
        pass


class MySQLConnection(DBConnection):
    def query(self, sql: str) -> list:
        print(f"[MySQL] Выполнение: {sql}")
        return [{"id": 1, "name": "Товар из MySQL"}]


class PostgreSQLConnection(DBConnection):
    def query(self, sql: str) -> list:
        print(f"[PostgreSQL] Выполнение: {sql}")
        return [{"id": 1, "name": "Товар из Postgres"}]


class ProductRepository:
    def __init__(self, db: DBConnection):
        self.db = db

    def find_all(self) -> list:
        return self.db.query("SELECT * FROM products")

    def find_by_id(self, id: int) -> dict:
        results = self.db.query(f"SELECT * FROM products WHERE id = {id}")
        return results[0] if results else {}


mysql_repo = ProductRepository(MySQLConnection())
print(mysql_repo.find_all())

pg_repo = ProductRepository(PostgreSQLConnection())
print(pg_repo.find_by_id(1))
