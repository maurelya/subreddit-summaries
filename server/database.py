#!/usr/bin/env python3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import EmailType

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///subreddit-summarizer.sqlite3'

db = SQLAlchemy(app)

class Users(db.Model):
   id = db.Column('user_id', db.Integer, primary_key = True)
   name = db.Column(db.String(100))
   email = db.Column(EmailType)
   subreddit = db.Column(db.String(100))

class Posts(db.Model):
  id = db.Column('post_id', db.Integer, primary_key=True)
  user_id = db.Column(db.Integer, db.ForeignKey('user_id'))
  title = db.Column(db.String(50))
  body_summary = db.Column(db.Text)
  top_comment_summary =  db.Column(db.Text)

# User methods

def add_user_record(new_record):
    db.session.add(new_record)
    db.session.commit()

def get_all_user_records():
   Users.query.all()

def get_user_by_email(email):
    Users.query.filter_by(email = email).all()

def get_user_by_id(id):
    Users.query.filter_by(user_id = id).all()

# Post methods

def add_post_record(new_record):
    db.session.add(new_record)
    db.session.commit()

def get_all_post_records():
   Posts.query.all()

def get_post_by_user(id):
    Posts.query.filter_by(user_id = id).all()

def get_post_by_id(id):
    Posts.query.filter_by(post_id = id).all()




    