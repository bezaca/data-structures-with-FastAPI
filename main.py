from typing import List
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from starlette.status import HTTP_200_OK

from crud import get_user_by_email, get_users_descending, get_users_ascending, get_user_by_id, delete_user
from database import SessionLocal, engine
import models
from schemas import User, UserCreate

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/user/", response_model=User)
def create_user(user: UserCreate, db: Session = Depends(get_db)):

    db_user = get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    create_user(db=db, user=user)

    return JSONResponse(status_code=status.HTTP_201_CREATED, content={'message': 'user created'})


@app.get("/user/descending_id", response_model=List[User])
def get_all_users_descending(db: Session = Depends(get_db)):

    users = get_users_descending(db)

    return JSONResponse(status_code=status.HTTP_200_OK, content=users)


@app.get("/user/descending_id", response_model=List[User])
def get_all_users_ascending(db: Session = Depends(get_db)):

    users = get_users_ascending(db)

    return JSONResponse(status_code=status.HTTP_200_OK, content=users)


@app.get("/user/{user_id}", response_model=User)
def get_one_user(user_id: int, db: Session = Depends(get_db)):

    user = get_user_by_id(db, user_id)
    if user:
        return JSONResponse(status_code=status.HTTP_200_OK, content=user)

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail="User not found")


@app.delete("/user/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = delete_user(db, user_id)

    return JSONResponse(status_code=status.HTTP_200_OK, content={'delete user': user})


@app.post("/blog_post/{user_id}")
def create_blog_post(user_id: int):
    ...


@app.get("/user/{user_id}")
def get_all_blog_posts(user_id: int):
    ...


@app.get("/blog_post/{blog_post_id}")
def get_one_blog_post(blog_post_id: int):
    ...


@app.delete("/blog_post/{blog_post_id}")
def delete_blog_post(blog_post_id: int):
    ...
