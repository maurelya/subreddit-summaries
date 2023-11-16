import sqlite3
from healthcheck import HealthCheck
from database.main.init_db import db


health = HealthCheck()

# add your own check function to the healthcheck
def sqlite_available():
    try:
        db.get_engine().connect()
    except Exception as e:
        print("sqlite_available: ", e)
        return 400, e
    
    return 200, "SQLite database is ok"

health.add_check(sqlite_available)
