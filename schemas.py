from pydantic import BaseModel
from datetime import date


class BlogPostBase(BaseModel):
    title: str
    body: str
    date: date


class BlogPostCreate(BaseModel):
    user_id: int


class BlogPost(BlogPostCreate):

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    name: str
    email: str
    address: str
    phone: int


class UserCreate(UserBase):
    pass


class User(UserBase):

    class Config:
        orm_mode = True
