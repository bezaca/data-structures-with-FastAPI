from sqlalchemy.orm import Session


import models
import schemas
import linked_list


def create_user(db: Session, user: schemas.UserBase):

    db_user = models.User(
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
    return db.query(models.User).filter(models.User.email == email).first()


def get_users_descending(db: Session, skip: int = 0):

    users = db.query(models.User).offset(skip).all()
    users_linkedlist = linked_list.LinkedList()

    for user in users:
        users_linkedlist.prepend({
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "address": user.address,
            "phone": user.phone,
        })

    return users_linkedlist
