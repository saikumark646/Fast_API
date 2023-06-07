from pydantic import BaseModel
from typing import Union


class UserCreation(BaseModel):
    username:str
    password:str
    email:str

class ShowUser(BaseModel):  # if class Config() is used then this schema model is used as response_model
    id:int
    username:str
    email:str
    class Config():
        orm_mode=True

class Login(BaseModel):
    username:str
    password:str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Union[str, None] = None
