
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import user

import crud
import models
import schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/user/")
def create_user(user: schemas.UserBase, db: Session = Depends(get_db)):

    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    crud.create_user(db=db, user=user)

    return JSONResponse(status_code=status.HTTP_201_CREATED, content={'message': 'user created'})

@app.get("/user/descending_id")
def get_all_users_descending(db: Session = Depends(get_db)):
    
    users = crud.get_users_descending()
    users.print_list()


@app.get("/user/descending_id")
def get_all_users_ascending():
    ...


@app.get("/user/{user_id}")
def get_one_user(user_id: int):
    ...


@app.delete("/user/{user_id}")
def delete_user(user_id: int):
    ...


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
