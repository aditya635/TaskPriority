from pydantic import BaseModel
from typing import Optional,List

class Task(BaseModel):
    name:str
    description:str
    priority:int
    class Config():
        orm_mode=True

class Tasks(BaseModel):
    name:str
    description:str
    priority:int
    user_id: int
    class Config():
        orm_mode=True

class ShowUser(BaseModel):
    name:str
    email:str
    tasks : Optional[List[Task]] = []
    class Config():
        orm_mode=True

class User(BaseModel):
    name:str
    email:str
    password:str



class Login(BaseModel):
    username:str
    password:str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None