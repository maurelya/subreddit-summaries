#!/usr/bin/env python3
import json
import requests
from flask import Flask
from models.users import Users, get_all_user_records
from scrape_reddit import scrape_subreddit

app = Flask(__name__)


'''
function to iterate through all the users
using API
'''

def collect_summarized_posts():
    # Query all rows in the `users` table
    users = get_all_user_records()

    for user in users:
        
        subreddit = user.subreddit
        scrape_subreddit(subreddit)
        

'''
function to get the top post and comments from a subreddit.
'''

def get_subreddit_post():
    response = requests.get("https://weatherdbi.herokuapp.com/data/weather/boulder")
    return response.json()["currentConditions"]["temp"]["c"]

'''
function to summarize the top post and comments.
'''

def summarize_post():
    response = requests.get("https://weatherdbi.herokuapp.com/data/weather/boulder")
    return response.json()["currentConditions"]["temp"]["c"]

'''
function to add a new post.
'''

def add_summarized_post():
    new_entry = Users(name=name, email=email)


'''
In main we first get the current temperature and then 
create a new object that we can add to the database. 
'''
if __name__ == "__main__":
    collect_summarized_posts()
    
    