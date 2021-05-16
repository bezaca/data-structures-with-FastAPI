from typing import List
from pydantic import BaseModel
from datetime import date

class BlogPostBase(BaseModel):
    title: str
    body: str
    date: date
    user_id: int

 
class BlogPost(BlogPostBase):

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    name: str
    email: str
    address: str
    phone: int

# class UserCreate(UserBase):
#     posts: List[BlogPostBase]


class User(UserBase):

    class Config:
        orm_mode = True
