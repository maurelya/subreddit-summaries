#!/usr/bin/env python3
import json, pika
import os

'''
Establish a connection to a RabbitMQ server.
localhost means we are connecting to the local
machine. However we can provide a IP address to
a different machine.
'''
channel = ""
def connect_rabbitmq():
    print("Connecting to rabbitmq")
    url = os.environ.get('CLOUDAMQP_URL', 'amqp://guest:guest@localhost:5672/%2f')
    params = pika.URLParameters(url)
    params.socket_timeout = 5
    conn = pika.BlockingConnection(params)    
    global channel
    channel = conn.channel()

    '''
    We create a queue just for emails
    '''
    channel.queue_declare(queue="emails")




def get_channel():
    return channel




