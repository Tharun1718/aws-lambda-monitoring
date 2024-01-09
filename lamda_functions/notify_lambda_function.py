import json
import requests

slack_webhook_url = 'https://hooks.slack.com/services/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'

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



