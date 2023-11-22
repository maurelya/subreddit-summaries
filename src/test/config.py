
import os


db_path = os.environ.get("DB_PATH")

class Config(object):
    DEBUG = False
    TESTING = False

class DevelopmentConfig(Config):
    ENV = "development"
    DEVELOPMENT = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///dev_subreddit-summarizer.sqlite3'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    
class TestingConfig(DevelopmentConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test_subreddit-summarizer.sqlite3'


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = db_path
    SQLALCHEMY_TRACK_MODIFICATIONS = True