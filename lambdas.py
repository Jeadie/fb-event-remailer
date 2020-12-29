import json
import requests
import os


# Handles webhook itself
def handler(event, context): 
    hook = json.loads(event["body"])
    event_changes = hook["entry"]["changes"]
    user = hook["entry"]["id"]

    # Verify User
    


# Handles creating Web hook
def handler(event, context): 
    app_access_token = requests.get(
        "https://graph.facebook.com/oauth/access_token",
        params= {
            "client_id": os.environ['FB_APP_ID'],
            "client_secret": os.environ["FB_APP_SECRET"],
            "grant_type": "client_credentials"
        }
    ).json()

    create_webhook = requests.post(
        f"https://graph.facebook.com/{os.environ['FB_APP_ID']}/subscriptions",
        data= {
          "object": "user",
          "callback_url": event['headers']['host'],
          "fields": "events",
          "verify_token": os.environ['FB_APP_VERIFY_TOKEN'],
          "access_token": app_access_token["access_token"]
        }
    )
    if requests.status_code != 200:
        print("ERROR: Could not make webhook")


# To handle challenge: 
def handler(event, context): 
    if event["queryStringParameters"]["hub.mode"] != "subscribe":
        print("Message not meant for me")

    if event["queryStringParameters"]["hub.verify_token"] != "123456":
        print("Failed verification token")

    return event["queryStringParameters"]["hub.challenge"]