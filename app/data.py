from models import User, UserRequest
from services.db_services import DB
from utils import get_password_hash


class UserMapper:

    @classmethod
    def find_by_id(cls, user_id: int) -> User:
        """Поиск пользователя по ID."""

        with DB() as db:
            db.execute("""
            SELECT id, username, password
            FROM users
            WHERE id = ?""", (user_id,))

            row = db.fetchone()

            return User(id=row[0], username=row[1], password=row[2]) if row else None

    @classmethod
    def find_by_username(cls, username: str) -> User:
        """Поиск пользователя по username."""

        with DB() as db:
            db.execute("""
            SELECT id, username, password
            FROM users
            WHERE username = ?""", (username,))

            row = db.fetchone()

            return User(id=row[0], username=row[1], password=row[2]) if row else None

    @classmethod
    def create(cls, user: UserRequest) -> int:
        """Создает запись с новым пользователем. Возвращает ID созданной записи."""

        with DB() as db:
            db.execute("""
            INSERT INTO users (username, password)
            VALUES (?, ?)""", (user.username, get_password_hash(user.password)))

            return db.lastrowid
