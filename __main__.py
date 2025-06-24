from dotenv import load_dotenv
import os
from datetime import datetime, timedelta
import time
import feedparser
import re
from twilio.rest import Client

load_dotenv()

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
sender_number = os.getenv("SENDER_NUMBER")
my_number = os.getenv("MY_NUMBER")

RSS_URL = os.getenv("RSS_URL")
COURSE_CODE = os.getenv("COURSE_CODE")

def extract_id(url: str) -> int:
    match = re.search(r'id=(\d+)', url)
    if match:
        number = match.group(1)
        return int(number)
    return None
def send_text_notification(entry):
    message = f"{entry.title} \nAuthor:{entry.author} \nLink: {entry.id}"
    client = Client(account_sid, auth_token)

    client.messages.create(
        body=message,
        from_=sender_number,
        to=my_number
    )
def check_updates():
    feed = feedparser.parse(RSS_URL)
    now = datetime.now()

    new_entries = []

    for entry in feed.entries:
        if hasattr(entry, "published_parsed"):
            entry_time = datetime.fromtimestamp(time.mktime(entry.published_parsed))
            if entry_time >= now - timedelta(days=3):
                new_entries.append(entry)

    print(new_entries)
    for entry in new_entries:
        send_text_notification(entry)

check_updates()

# while True:
#     now = datetime.now()
#     if now.hour == 2 and now.minute == 0 and now.second == 0:
#         check_updates()
#     time.sleep(3600*24-2)

