import pytest
from src.main.app import app
from src.test.config import config
from src.main.database.init_db import db
from user import User

@pytest.fixture
def client():
    app.config.from_object(config.TestingConfig)
    with app.test_client() as client:
        with app.app_context():
            yield client


#tests/conftest.py
@pytest.fixture()
def init_database():

    db.create_all()

    test_users = [
        {"name": "Test User 1", "email": "test1@gmail.com", "subreddit": "tacos"},
        {"name": "Test User 2", "email": "test2@gmail.com", "subreddit": "cats"},
        {"name": "Test User 3", "email": "test3@gmail.com", "subreddit": "cars"},
    ]

    def create_post_model(user):
        return User(**user)

    mapped_users = map(create_post_model, test_users)
    t_users = list(mapped_users)

    db.session.add_all(t_users)

    db.session.commit()

    yield db 
    
    db.session.close()  
    db.drop_all()