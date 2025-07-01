from dotenv import load_dotenv
import os
from datetime import datetime, timedelta
import time
import feedparser
from twilio.rest import Client
from models import Entry
from utils import sleep_until, write_message

# environment variables
load_dotenv()
RSS_URL = os.getenv("RSS_URL")
COURSE_CODE = os.getenv("COURSE_CODE")

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
sender_number = os.getenv("SENDER_NUMBER")
my_number = os.getenv("MY_NUMBER")


def send_notification(entry: Entry) -> None:
    message = write_message(entry)
    client = Client(account_sid, auth_token)

    client.messages.create(
        body=message,
        from_=sender_number,
        to=my_number
    )

def check_updates() -> None:
    print("steva")
    # feed = feedparser.parse(RSS_URL)
    # now = datetime.now()
    # new_entries = []

    # for entry in feed.entries:
    #     if hasattr(entry, "published_parsed"):
    #         entry_time = datetime.fromtimestamp(time.mktime(entry.published_parsed))
    #         if entry_time >= now - timedelta(days=3):
    #             new_entries.append(entry)

    # for entry in new_entries:
    #     send_notification(entry)


checkup_time = datetime.now()
checkup_time = checkup_time.replace(hour=5, minute=9, second=0, microsecond=0)

while True:
    sleep_until(checkup_time)
    print("steva")
    # check_updates()
