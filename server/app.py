#!/usr/bin/env python3

from flask import Flask
from flask_cors import CORS
from flask import Flask, request
from datacollector.main.data_collector import collect_all_posts

from database.main.init_db import setup_db
from database.main.models.posts import Posts, add_post_record
from reddit.main.scrape_reddit import setup_praw
from database.main.models.users import Users, add_user_record


app = Flask(__name__)


setup_db(app)
setup_praw()

if __name__ == '__main__':
    app.run(host='localhost', port=5000)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# add a new user to the User table
@app.route('/add-user', methods=['POST'])
def add_user():
    try:
        content = request.get_json()
        new_user = Users(name = content['name'],
                        email = content['email'],
                        subreddit = content['subreddit'])
        
        add_user_record(new_user)
        return 'OK'
    except Exception as e:
        print("Encounter error in /add-user api:", e)
        return 'Not OK'
    

    
# gell all posts and comments from reddit
@app.route('/get-all-posts', methods=['GET'])
def get_all_posts():
    try:
        collect_all_posts()
        return 'OK'
    except Exception as e:
        print("Encounter error in /get-all-posts api:", e)
        return 'Not OK'
    

# add a new post to Post table
@app.route('/add-post', methods=['POST'])
def add_post():
    try:
        content = request.get_json()

        new_post = Posts(user_id = content['user_id'],
                        title = content['title'],
                        subreddit = content["subreddit"],
                        top_post_body = content['top_post_body'],
                        top_comment = content["top_comment"],
                        created_utc = content["created_utc"],
                        url = content["url"],
                        top_post_summary = content['top_post_summary'],
                        summary_sentiment = content['summary_sentiment'])
        
        add_post_record(new_post)
        return 'OK'
    except Exception as e:
        print("Encounter error in /add-post api:", e)
        return 'Not OK'