import json
import requests
import os

slack_webhook_url = os.getenv('webhook_url')

def lambda_handler(event, context):
    try:
        send_slack_alert()
        return {
        'statusCode': 200,
        'body': json.dumps('Message sent successfully!')
        }
    except Exception as e:
        return {
        'body': json.dumps('Error sending message')
        }


def send_slack_alert():
    payload = {
        'text': "Your database is down"
    }
    requests.post(slack_webhook_url, json=payload)



