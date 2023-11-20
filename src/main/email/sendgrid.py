import json
import os
import sendgrid
from sendgrid.helpers.mail import  Email, Mail, To

template_id=os.environ.get("TEMPLATE_ID")
sg = sendgrid.SendGridAPIClient(os.environ.get("SENDGRID_API_KEY"))
from_email = Email(os.environ.get("FROM_EMAIL"))

def generate_email(email, subreddit, post_summary, post_url, emotion ):
    to_email = To(email)
    
    subject = "Subreddit Summarizer Email"

    mail = Mail(from_email, to_email,subject )


    mail.dynamic_template_data = {
    'subreddit': subreddit,
    'post_summary': post_summary,
    'post_url': post_url,
    'emotion': emotion
    }
    mail.template_id = template_id

    response = sg.client.mail.send.post(request_body=mail.get())
    print("mail response: ", response)
