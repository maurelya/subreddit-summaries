import praw
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

praw_clientsecret = os.environ['PRAW_CLIENT_SECRET']
praw_clientid = os.environ['PRAW_CLIENT_ID']
reddit = ""

options = Options()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)

def setup_praw():
    print("Setting up PRAW \n")
    user_agent = "Scraper 1.0 by /u/reddit_summarizer"


    global reddit   
    reddit = praw.Reddit(
        client_id = praw_clientid,
        client_secret = praw_clientsecret,
        user_agent=user_agent,
        webdriver=driver
    )

def scrape_subreddit(subreddit):
    print("Generating subreddit headlines dataframe. \n")
    submission_list = []

    for submission in reddit.subreddit(subreddit).hot(limit=1):
        post_obj = {'post_title': submission.title,
                    'post_body': submission.selftext, 
                    'top_comment': submission.comments[0].body,
                    'created_utc': submission.created_utc,
                    'url': submission.url}
        submission_list.append(post_obj)


    driver.quit()
    return submission_list[0]