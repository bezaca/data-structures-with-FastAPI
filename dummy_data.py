from faker import Faker
from random import randrange

from crud import create_user, create_blogpost
from database import SessionLocal 
from models import BlogPost, User

faker = Faker()


db = SessionLocal()

for _ in range(100):

    name = faker.name()
    address = faker.address()
    phone = faker.msisdn()
    email = f'{name.replace(" ", "_")}@email.com'

    new_user = User(name=name, address=address, phone=phone, email=email)
    create_user(db=db, user=new_user)

for _ in range(100):

    title = faker.sentence(5)
    body = faker.paragraph(190)
    date = faker.date_time()
    user_id = randrange(1, 100)

    new_post = BlogPost(title=title, body=body, date=date)
    create_blogpost(db=db, blogpost=new_post, user_id=user_id)
    
db.close()

#TODO: Add rich library to get visual feedback