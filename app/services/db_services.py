import sqlite3


class DB:
    def __enter__(self) -> None:
        self.conn = sqlite3.connect('users.db')
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.conn.commit()
        self.conn.close()


def init_db() -> None:
    """Создает таблицу пользователей, если она еще не создана."""

    with DB() as db:
        db.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
        """)
