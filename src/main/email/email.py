#!/usr/bin/env python3
from flask import Flask
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
        users = get_all_user_records()

        for user in users:
            post = get_recent_post(user.id)
            print("post: ", post)
            generate_email(user.email, post.subreddit, post.top_post_summary, post.url, post.summary_sentiment)
        
    except Exception as error:
            print("An exception occurred:", error)

    
    