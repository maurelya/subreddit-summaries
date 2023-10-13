from init_db import db

class Posts(db.Model):
    id = db.Column('post_id', db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    title = db.Column(db.String(50))
    body_summary = db.Column(db.Text)
    top_comment_summary =  db.Column(db.Text)

    def __init__(self, user_id, title, body_summary, top_comment_summary):
        self.user_id = user_id
        self.title = title
        self.body_summary = body_summary
        self.top_comment_summary = top_comment_summary

# Post methods

def add_post_record(new_record):
    db.session.add(new_record)
    db.session.commit()

def get_all_post_records():
    return Posts.query.all()

def get_post_by_user(id):
    return Posts.query.filter_by(user_id = id).all()

def get_post_by_id(id):
    return Posts.query.filter_by(post_id = id).all()