import pandas as pd
import praw
from gologin import GoLogin
from selenium.webdriver import Chrome


# Set up a GoLogin profile
gl = GoLogin({
"token": "yU0token",
})

def setup_golin():
    profile_id = gl.create({
        "name":"my-profile",
        "browser_executable_path": "/path/to/chrome.exe",
        "user_agent": "my-user-agent",
        "proxy": {
        "server": "my-proxy-server",
        "port": 1234,
        "username": "my-username",
        "password": "my-password"
        }
    })
    return gl.getProfile(profile_id)

def get_golin_webdriver():
    driver = setup_golin().get_webdriver("my-profile", Chrome)
    return driver


def setup_praw():
    user_agent = "Scraper 1.0 by /u/python_engineer"

    reddit = praw.Reddit(
    client_id="****",
    client_secret="****",
    user_agent=user_agent,
    webdriver=get_golin_webdriver()
    )
    return reddit

def scrape_subreddit(subreddit):
    headlines = set ( )
    reddit = setup_praw()

    for submission in reddit.subreddit(subreddit).hot(limit=3):
        headlines.add(submission.title)
        print(len(headlines))

    df = pd.DataFrame(headlines)

    return df