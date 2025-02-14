from pydantic import BaseModel


class User(BaseModel):
    id: int
    username: str
    password: str


class UserResponse(BaseModel):
    id: int
    username: str


class UserRequest(BaseModel):
    username: str
    password: str


class AccessToken(BaseModel):
    access_token: str
    token_type: str = 'bearer'
