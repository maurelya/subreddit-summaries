#!/usr/bin/env python3
import requests
from flask import Flask
from server.models.users import Users, Posts


app = Flask(__name__)

    
'''
Helper function to get temperature
using API
'''

def get_top_posts():
    response = requests.get("https://weatherdbi.herokuapp.com/data/weather/boulder")
    return response.json()["currentConditions"]["temp"]["c"]


'''
In main we first get the current temperature and then 
create a new object that we can add to the database. 
'''
if __name__ == "__main__":
    current_temperature = get_top_posts()
    new_entry = Users(name=name, email=email)
    