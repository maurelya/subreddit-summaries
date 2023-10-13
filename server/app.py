#!/usr/bin/env python3

from flask import Flask
from flask_cors import CORS
from flask import Flask, request
from data_collector import collect_summarized_posts
from models.users import add_user_record, Users
from server.init_db import setup_db
from models.posts import Posts, add_post_record


app = Flask(__name__)


setup_db(app)

if __name__ == '__main__':
    app.run(host='localhost', port=5000)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# add a new user
@app.route('/add-user', methods=['POST'])
def add_user():
    try:
        content = request.get_json()
        new_user = Users(name = content['name'], email = content['email'], subreddit = content['subreddit'])
        add_user_record(new_user)
        collect_summarized_posts()
        return 'OK'
    except Exception as e:
        print("Encounter error in /add-user api:", e)
        return 'Not OK'
    

# add a new post
@app.route('/add-post', methods=['POST'])
def add_post():
    try:
        content = request.get_json()
        new_post = Posts(user_id = content['name'], title = content['email'],
                          body_summary = content['subreddit'], top_comment_summary = content[""])
        add_post_record(new_post)
        return 'OK'
    except Exception as e:
        print("Encounter error in /add-post api:", e)
        return 'Not OK'