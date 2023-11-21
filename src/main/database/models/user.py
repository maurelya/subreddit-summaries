#!/usr/bin/env python3
from dataclasses import dataclass
from sqlalchemy_utils import EmailType
from src.main.database.init_db import db


@dataclass
class User(db.Model):
    id: int
    name: str
    email: str
    subreddit: str

    id = db.Column('user_id', db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    email = db.Column(EmailType)
    subreddit = db.Column(db.String(100))

    def __init__(self, name, email, subreddit):
        self.name = name
        self.email = email
        self.subreddit = subreddit
    


# User methods

def add_user_record(new_record):
    db.session.add(new_record)
    db.session.commit()
    

def get_all_user_records():
   return User.query.all()

def get_user_by_email(email):
    return User.query(User).filter_by(email = email).all()

def get_user_by_id(id):
    return User.query(User).filter_by(user_id = id).all()
