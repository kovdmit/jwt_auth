from datetime import timedelta, datetime

import jwt
from fastapi import (
    Depends,
    status,
    HTTPException,
)

from config import (
    SECRET_KEY,
    ACCESS_TOKEN_EXPIRE_MINUTES,
    ALGORITHM,
    oauth2_scheme,
)


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({'exp': expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def get_user_from_token(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload.get('sub')
    except jwt.ExpiredSignatureError:
        HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Время истекло.',
            headers={'WWW-Authenticate': 'Bearer'},
        )
    except jwt.InvalidTokenError:
        HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Некорректный токен.',
            headers={'WWW-Authenticate': 'Bearer'},
        )
