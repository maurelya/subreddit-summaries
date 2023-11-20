#!/usr/bin/env python3

import json
from flask import Flask, render_template
from flask_cors import CORS
from flask import Flask, request


from prometheus_flask_exporter import PrometheusMetrics
from main.email.email import send_emails
from main.email.sendgrid import generate_email
from main.event_collaboration.rabbitmq import connect_rabbitmq

from src.main.database.init_db import setup_db
from src.main.database.models.posts import Posts, add_post_record
from src.main.database.models.users import Users, add_user_record
from src.main.datacollector.data_collector import collect_all_posts
from src.main.reddit.scrape_reddit import setup_praw
from src.main.healthcheck.healthcheck import health

app = Flask(__name__)


setup_db(app)
setup_praw()
connect_rabbitmq()

metrics = PrometheusMetrics(app)
if __name__ == '__main__':
    
    app.run(host='localhost', port=27000)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})



@app.route("/")
def index():
    return render_template("index.html")

# get app health check data
app.add_url_rule("/healthcheck", "healthcheck", view_func=lambda: health.run())


# add a new user to the User table
@metrics.gauge('add_new_user', 'add a new user to the User table')
@app.route('/add_user', methods=['POST'])
def add_user():
    try:
        name = request.form['name']
        email = request.form['email']
        subreddit = request.form['subreddit']
        new_user = Users(name, email, subreddit)
        
        add_user_record(new_user)
        return 'OK'
    except Exception as e:
        print("Encounter error in /add_user api:", e)
        return 'Not OK'
    

    
# gell all posts and comments from reddit
@app.route('/get_all_posts', methods=['GET'])
def get_all_posts():
    try:
        collect_all_posts()
        return 'OK'
    except Exception as e:
        print("Encounter error in /get_all_posts api:", e)
        return 'Not OK'
       

# add a new post to Post table
@app.route('/add_post', methods=['POST'])
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
        print("Encounter error in /add_post api:", e)
        return 'Not OK'
    
# send a single email
@app.route('/send_email', methods=['POST'])
def send_email():
    try:
        content = request.get_json()
        print("content: ", json.dumps(content, indent=4))

        email = content['email']
        subreddit = content['subreddit']
        post_summary = content['post_summary']
        post_url = content['post_url']
        emotion = content['emotion']

        generate_email(email, subreddit,post_summary, post_url, emotion)
        return 'OK'
    except Exception as e:
        print("Encounter error in /send_email api:", e)
        return 'Not OK'

# send all emails
@app.route('/send_all_emails', methods=['GET'])
def send_all_emails():
    try:
        send_emails()
        return 'OK'
    except Exception as e:
        print("Encounter error in /send_emails api:", e)
        return 'Not OK'