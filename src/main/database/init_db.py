import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

database_path = os.environ.get("DB_PATH")


def get_database_path():
    return database_path

def setup_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path

    with app.app_context():
        db.init_app(app)
        db.create_all()

