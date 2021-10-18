from pydantic import BaseModel
from typing import Optional

class ShowUser(BaseModel):
    name:str
    email:str
    class Config():
        orm_mode=True

class User(BaseModel):
    name:str
    email:str
    password:str

class Task(BaseModel):
    name:str
    description:str
    priority:int
    class Config():
        orm_mode=True

class Login(BaseModel):
    username:str
    password:str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None