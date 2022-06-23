#Python
from uuid import UUID
from datetime import date
from typing import Optional

from pydantic import BaseModel
from pydantic import Field
from pydantic import EmailStr

from fastapi import FastAPI



app = FastAPI()


#Models
class UserBase(BaseModel):
    user_id: UUID = Field(...)
    email: EmailStr = Field(...)


class UserLogin(UserBase):
    password: str = Field(..., min_length=8)

class User(UserBase):
    first_name: str = Field(..., min_length=1, max_length=50)
    last_name: str = Field(..., min_length=1, max_length=50)
    birth_date: Optional[date] = Field(default=None)


class Tweet(BaseModel):
    pass


@app.get(path="/")
def home():
    return {"twitter api": "working"}