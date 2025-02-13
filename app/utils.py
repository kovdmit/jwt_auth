from config import pwd_context


def get_password_hash(password: str) -> str:
    """Хэширует пароль."""

    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Проверяет правильность хэша и пароля."""

    return pwd_context.verify(plain_password, hashed_password)
