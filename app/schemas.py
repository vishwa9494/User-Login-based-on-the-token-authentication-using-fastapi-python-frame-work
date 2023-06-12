from pydantic import BaseModel,EmailStr
from datetime import datetime
from typing import Optional
from pydantic.types import conint

class UserCreate(BaseModel):
    email :EmailStr
    password :str 


class Posta(BaseModel):
    id : int
    title : str
    content : str


class PostOut(BaseModel):
    id:int
        
    class Config:
        orm_mode = True






class UserOut(BaseModel):
    id : int
    email : EmailStr

    class Config:
        orm_mode =True


class UserLogin(BaseModel):
    email : EmailStr
    password : str





class Token(BaseModel):
    access_token : str
    token_type : str


class TokenData(BaseModel):
    id : Optional[str]= None


class Vote(BaseModel):
    post_id:int
    dir:conint(le=1) 