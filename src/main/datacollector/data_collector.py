#!/usr/bin/env python3
import requests
from flask import Flask

from src.main.reddit.scrape_reddit import scrape_subreddit
from src.main.database.models.users import get_all_user_records
from src.main.watsonx.watsonx_ai import sentiment_analysis, summarize_post

app = Flask(__name__)


'''
function to iterate through all the users
using API
'''

def collect_all_posts():
    # Query all rows in the `users` table
    try:
        users = get_all_user_records()

        for user in users:
            post_obj_list = scrape_subreddit(user.subreddit)

            post_title = post_obj_list["post_title"]
            post_body = post_obj_list['post_body']
            top_comment = post_obj_list['top_comment']
            summary = summarize_post(user.subreddit, post_title, post_body, top_comment)
            summary_sentiment = sentiment_analysis(user.subreddit, summary)

            print("summary: ", summary)

            body = {'user_id': user.id, 
                    'title': post_title,
                    'subreddit': user.subreddit, 
                    'top_post_body': post_body,
                    'top_comment': top_comment, 
                    'created_utc': post_obj_list['created_utc'], 
                    'url': post_obj_list['url'],
                    'top_post_summary': summary,
                    'summary_sentiment': summary_sentiment}
        
            response = requests.post("/add_post", json = body)
            print(response)
          
        
    except Exception as error:
            print("An exception occurred:", error)

    
    