from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db = SQLAlchemy()

database_path = 'sqlite:///subreddit-summarizer.sqlite3'


def get_database_path():
    return database_path

def setup_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path

    with app.app_context():
        db.init_app(app)
        db.create_all()

def get_sql_session():
    engine = create_engine(get_database_path())
    new_session = sessionmaker(bind=engine)
    return new_session()

