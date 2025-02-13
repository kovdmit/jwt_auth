import sqlite3

from fastapi import Depends, APIRouter, HTTPException, status

from models import UserResponse, UserRequest, AccessToken
from data import UserMapper
from services.token_services import create_access_token, get_username_from_token
from utils import verify_password

router = APIRouter()


@router.post('/register')
async def register(request_user: UserRequest) -> AccessToken:
    """Регистрация пользователей."""

    try:
        user_id = UserMapper.create(request_user)
    except sqlite3.IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={'error': 'Username already exists'}
        )
    else:
        user = UserMapper.find_by_id(user_id)

        return AccessToken(access_token=create_access_token({'sub': user.username}))


@router.post('/auth')
async def auth(request_user: UserRequest):
    """Аутентификация пользователей. Возвращает access JWT токен."""

    user = UserMapper.find_by_username(request_user.username)
    if user and verify_password(request_user.password, user.password):
        return AccessToken(access_token=create_access_token({'sub': user.username}))
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={'error': 'Invalid credentials'}
        )


@router.get('/me', response_model=UserResponse)
async def me(username: str = Depends(get_username_from_token)):
    """Возвращает информацию о пользователе."""

    user = UserMapper.find_by_username(username)

    if user:
        return user
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={'error': 'User not found'}
        )
