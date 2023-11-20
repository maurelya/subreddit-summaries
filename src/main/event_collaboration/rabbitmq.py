#!/usr/bin/env python3
import json, pika

'''
Establish a connection to a RabbitMQ server.
localhost means we are connecting to the local
machine. However we can provide a IP address to
a different machine.
'''
channel = ""
def connect_rabbitmq():
    print("Connecting to rabbitmq")
    conn = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    global channel
    channel = conn.channel()

    '''
    We create a queue just for emails
    '''
    channel.queue_declare(queue="emails")




def get_channel():
    return channel




