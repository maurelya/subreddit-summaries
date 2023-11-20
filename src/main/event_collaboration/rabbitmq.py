#!/usr/bin/env python3
import json, pika
from flask import request
import os

import requests

from main.email.sendgrid import generate_email

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




def summarized_posts_callback(ch, method, properties, body):
    body = json.loads(body)
    print(" [x] Received %r" % body)
    response = requests.post( 'http://' + request.host + "/add_post", json = body)
    print(response)



def consume_summarized_posts():
    print("Consuming summarized posts")
    channel.basic_consume(queue='summarized_posts', on_message_callback=summarized_posts_callback, auto_ack=True)

    channel.basic_cancel('summarized_posts')


def emails_callback(ch, method, properties, body):
    body = json.loads(body)
    print(" [x] Received %r" % body)
    generate_email(body.email, body.subreddit, body.top_post_summary, body.url, body.summary_sentiment)

def consume_emails():
    print("Consuming emails")
    channel.basic_consume(queue='emails', on_message_callback=emails_callback, auto_ack=True)

    channel.basic_cancel('emails')
    

def get_channel():
    conn =  get_rabbitmq_conn()
    return conn.channel()




