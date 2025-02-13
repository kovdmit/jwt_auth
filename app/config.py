import os

from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from dotenv import load_dotenv


load_dotenv()


oauth2_scheme = OAuth2PasswordBearer(tokenUrl='auth')

SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITH = os.getenv('ALGORITH')
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
