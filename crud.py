from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import now

from models import User, BlogPost
import schemas
from linked_list import LinkedList
from hash_table import HashTable


def create_blogpost(db: Session, blogpost: schemas.BlogPostCreate, user_id: int):

    db_blogpost = BlogPost(
        title=blogpost.title,
        body=blogpost.body,
        date=blogpost.date,
        user_id=user_id,
    )
    db.add(db_blogpost)
    db.commit()
    db.refresh(db_blogpost)
    return db_blogpost


def create_user(db: Session, user: schemas.UserCreate):

    db_user = User(
        name=user.name,
        email=user.email,
        address=user.address,
        phone=user.phone,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def get_users_descending(db: Session, skip: int = 0):

    users = db.query(User).offset(skip).all()
    users_linkedlist = LinkedList()

    for user in users:
        users_linkedlist.prepend({
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "address": user.address,
            "phone": user.phone,
        })

    return users_linkedlist.to_list()


def get_users_ascending(db: Session, skip: int = 0):

    users = db.query(User).offset(skip).all()
    users_linkedlist = LinkedList()

    for user in users:
        users_linkedlist.append({
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "address": user.address,
            "phone": user.phone,
        })

    return users_linkedlist.to_list()


def get_user_by_id(db: Session, user_id: int):

    users = db.query(User).all()
    users_linkedlist = LinkedList()

    for user in users:
        users_linkedlist.append({
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "address": user.address,
            "phone": user.phone,
        })

    find_user = users_linkedlist.get_user_by_id(user_id)

    return find_user


def delete_user_by_id(db: Session, user_id: int):

    db_user = db.query(User).filter(User.id == user_id).first()
    db.delete(db_user)
    db.commit()

    return db_user
