#!/usr/bin/env python3

from flask import Flask
from flask_cors import CORS
from flask import Flask, request
from models.users import add_user_record, Users
from init import setup_db


app = Flask(__name__)
setup_db(app)
if __name__ == '__main__':
    app.run(host='localhost', port=5000)



# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# sanity check route
@app.route('/submit', methods=['POST'])
def submit():
    content = request.get_json()
    print(content)
    new_user = Users(name = content['name'], email = content['email'], subreddit = content['subreddit'])
    add_user_record(new_user)
    return 'OK'