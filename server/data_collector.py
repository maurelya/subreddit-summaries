#!/usr/bin/env python3
import requests
from flask import Flask
from models.users import get_all_user_records
from scrape_reddit import scrape_subreddit
from watsonx_ai import send_to_watsonxai

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

            body = {'user_id': user.id, 
                    'title': post_obj_list["post_title"],
                    'subreddit': user.subreddit, 
                    'top_post_body': post_obj_list['post_body'],
                    'top_comment': post_obj_list['top_comment'], 
                    'created_utc': post_obj_list['created_utc'], 
                    'url': post_obj_list['url'],
                    'top_post_body_summary': '',
                    'top_comment_summary': '' }
            
            response = requests.post("http://127.0.0.1:5000/add-post", json = body)
            print(response)
            
            
        
    except Exception as error:
            print("An exception occurred:", error)

def augment( template_in, context_in, query_in ):
    return template_in % ( context_in,  query_in )          

'''
function to summarize the top post and comments.
'''
def summarize_post():
    prompt = """
    Article:
    ###
    %s
    ###

    Answer the following question using only information from the article. 
    Answer in a complete sentence, with proper capitalization and punctuation. 
    If there is no good answer in the article, say "I don't know".

    Question: %s
    Answer: 
    """
    send_to_watsonxai(prompt=prompt,
                    model_name="google/flan-ul2",
                    decoding_method="greedy",
                    max_new_tokens=100,
                    min_new_tokens=30,
                    temperature=1.0,
                    repetition_penalty=2.0)
    
    