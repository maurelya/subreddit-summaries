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

    channel = conn.channel()

    print("Created emails queue")
    channel.queue_declare(queue="emails")

    print("Created summarized_posts queue")
    channel.queue_declare(queue="summarized_posts")




def summarized_posts_callback(channel, method_frame, body):
    
    print('Recieved with body: ', json.dumps(body, indent=4))
    url = 'http://' + request.host + "/add_post"
    print(" add post url %r" % url)
    response = requests.post( url, json = body)
    print("response: ", response)
    channel.basic_ack(method_frame.delivery_tag)



def consume_summarized_posts():
    print("Consuming summarized posts")
    channel = get_channel()

    for message in channel.consume("summarized_posts", inactivity_timeout=1):
            if message == (None, None, None):
                 break
            body = message
            
            json_body = json.loads(body[2])
            method_frame = body[0]
            
            summarized_posts_callback(channel, method_frame, json_body)


def emails_callback(channel, method_frame, body):
    print('Recieved with body: ', json.dumps(body, indent=4))
    
    generate_email(body['email'], body['subreddit'], body['top_post_summary'], body['url'], body['summary_sentiment'])
    channel.basic_ack(method_frame.delivery_tag)

def consume_all_emails():
    print("Consuming emails")
    channel = get_channel()

    for message in channel.consume("emails", inactivity_timeout=1):
            if message == (None, None, None):
                 break
            body = message
            
            json_body = json.loads(body[2])
            method_frame = body[0]
            
            emails_callback(channel, method_frame, json_body)
    

def get_channel():
    conn =  get_rabbitmq_conn()
    return conn.channel()




