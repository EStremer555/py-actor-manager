import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str):
        self.db_name = db_name
        self.table_name = table_name
        self.conn = sqlite3.connect(self.db_name)

    def create(self, first_name: str, last_name: str):
        self.conn.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )

    def all(self):
        actor_cursor = self.conn.execute(
            f"SELECT * FROM {self.table_name}"
        )
        return [Actor(*row) for row in actor_cursor]

    def update(self, pk: int, first_name: str, last_name: str):
        self.conn.execute(
            f"UPDATE {self.table_name} SET first_name=?, last_name=? WHERE pk=?",
            (first_name, last_name, pk)
        )
        self.conn.commit()

    def delete(self, pk: int):
        self.conn.execute(
            f"DELETE FROM {self.table_name} WHERE pk=?",
            (pk,)
        )
        self.conn.commit()