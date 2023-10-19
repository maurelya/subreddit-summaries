from dataclasses import dataclass
from init_db import db

@dataclass
class Posts(db.Model):
    id: int
    user_id: int
    subreddit: str
    title: str
    top_post_body: str
    top_comment: str
    top_post_body_summary: str
    top_comment_summary: str
    created_utc: str
    url: str

    id = db.Column('post_id', db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    title = db.Column(db.String(100))
    subreddit = db.Column(db.String(100))
    top_post_body = db.Column(db.Text, nullable=True)
    top_comment =  db.Column(db.Text)
    top_post_body_summary = db.Column(db.Text, nullable=True)
    top_comment_summary =  db.Column(db.Text, nullable=True)
    created_utc = db.Column(db.Text)
    url = db.Column(db.Text)

    def __init__(self,
                user_id, 
                title, 
                subreddit,
                top_post_body,
                top_comment, 
                top_post_body_summary,
                top_comment_summary,
                created_utc,
                url):
        
        self.user_id = user_id
        self.title =  title
        self.subreddit = subreddit
        self.top_post_body = top_post_body
        self.top_comment = top_comment
        self.top_post_body_summary = top_post_body_summary
        self.top_comment_summary = top_comment_summary
        self.created_utc = created_utc
        self.url = url

# Post methods

def add_post_record(new_record):
    db.session.add(new_record)
    db.session.commit()

def update_post_record(id, top_post_body, top_comment):
    post = get_post_by_user(id)
    post.top_post_body_summary = top_post_body
    post.top_comment_summary = top_comment
    db.session.commit()

def get_all_post_records():
    return Posts.query.all()

def get_post_by_user(id):
    return Posts.query.filter_by(user_id = id).all()

def get_post_by_id(id):
    return Posts.query.filter_by(post_id = id).all()