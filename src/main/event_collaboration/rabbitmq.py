#!/usr/bin/env python3
import json, pika
from flask import request
import os

import requests

from src.main.email.sendgrid import generate_email

'''
Establish a connection to a RabbitMQ server.
localhost means we are connecting to the local
machine. However we can provide a IP address to
a different machine.
'''
channel = ""

def get_rabbitmq_conn():
    print("Get rabbitmq connection")
    url = os.environ.get('CLOUDAMQP_URL', 'amqp://guest:guest@localhost:5672/%2f')
    params = pika.URLParameters(url)
    params.socket_timeout = 5
    conn = pika.BlockingConnection(params)
    return conn

def connect_rabbitmq():
    print("Connecting to rabbitmq")
    conn = get_rabbitmq_conn()  
    global channel
    channel = conn.channel()

    print("Created emails queue")
    channel.queue_declare(queue="emails")

    print("Created summarized_posts queue")
    channel.queue_declare(queue="summarized_posts")




def summarized_posts_callback(body):
    print('Recieved with body: ', json.dumps(body, indent=4))
    url = 'http://' + request.host + "/add_post"
    print(" add post url %r" % url)
    response = requests.post( url, json = body)
    print("response: ", response)



def consume_summarized_posts():
    print("Consuming summarized posts")

    for message in channel.consume("summarized_posts", inactivity_timeout=1):
            if message == (None, None, None):
                 break
            body = message
            
            json_body = json.loads(body[2])
            
            summarized_posts_callback(json_body)


def emails_callback(body):
    print('Recieved with body: ', json.dumps(body, indent=4))
    
    generate_email(body['email'], body['subreddit'], body['top_post_summary'], body['url'], body['summary_sentiment'])

def consume_all_emails():
    print("Consuming emails")

    for message in channel.consume("emails", inactivity_timeout=1):
            if message == (None, None, None):
                 break
            body = message
            
            json_body = json.loads(body[2])
            
            emails_callback(json_body)
    

def get_channel():
    conn =  get_rabbitmq_conn()
    return conn.channel()




