#!/usr/bin/env python3
import json
from flask import Flask
from main.event_collaboration.rabbitmq import get_channel
from src.main.email.sendgrid import generate_email
from src.main.database.models.posts import get_recent_post


from src.main.database.models.users import get_all_user_records


app = Flask(__name__)


'''
function to iterate through all the users
using API
'''

def send_emails():
    # Query all rows in the `users` table
    
    try:
        channel = get_channel()
        users = get_all_user_records()

        for user in users:
            post = get_recent_post(user.id)

            channel.basic_publish(exchange="", routing_key="emails", body=json.dumps(
                 {"email": user.email, 
                  "subreddit": post.subreddit, 
                  "top_post_summary": post.top_post_summary, 
                  "url": post.url, 
                  "summary_sentiment": post.summary_sentiment}))
            
        
    except Exception as error:
            print("An exception occurred:", error)

    
    