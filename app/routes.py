from fastapi import Depends, APIRouter

from app.models import User
from data import USERS_DATA
from services import create_access_token, get_user_from_token
from utils import verify_password


router = APIRouter()


@router.post('/login')
async def login(user: User):
    user_data = USERS_DATA.get(user.username)
    if user_data and verify_password(user.password, user_data.get('password')):
        return {
            'access_token': create_access_token({'sub': user.username}),
            'token_type': 'bearer',
        }
    return {'error': 'Invalid credentials'}


@router.get('/me')
async def about_me(username: str = Depends(get_user_from_token)):
    user = USERS_DATA.get(username)

    return {'username': user.get('username')} if user else {'error': 'User not found'}
