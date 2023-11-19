from dataclasses import dataclass
from src.main.database.init_db import db

@dataclass
class Posts(db.Model):
    id: int
    user_id: int
    subreddit: str
    title: str
    top_post_body: str
    top_comment: str
    top_post_summary: str
    created_utc: str
    url: str
    summary_sentiment: str

    id = db.Column('post_id', db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    title = db.Column(db.String(100))
    subreddit = db.Column(db.String(100))
    top_post_body = db.Column(db.Text)
    top_comment =  db.Column(db.Text)
    top_post_summary = db.Column(db.Text)
    created_utc = db.Column(db.Text)
    url = db.Column(db.Text)
    summary_sentiment = db.Column(db.String(10))

    def __init__(self,
                user_id, 
                title, 
                subreddit,
                top_post_body,
                top_comment, 
                top_post_summary,
                created_utc,
                url,
                summary_sentiment):
        
        self.user_id = user_id
        self.title =  title
        self.subreddit = subreddit
        self.top_post_body = top_post_body
        self.top_comment = top_comment
        self.top_post_summary = top_post_summary
        self.created_utc = created_utc
        self.url = url
        self.summary_sentiment = summary_sentiment

# Post methods

def add_post_record(new_record):
    db.session.add(new_record)
    db.session.commit()

def update_post_record(id, top_post_body):
    post = get_post_by_user(id)
    post.top_post_summary = top_post_body
    db.session.commit()

def get_all_post_records():
    return Posts.query.all()

def get_post_by_user(id):
    return Posts.query.filter_by(user_id = id).all()

def get_post_by_id(id):
    return Posts.query.filter_by(post_id = id).all()