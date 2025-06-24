from dotenv import load_dotenv
import os
from datetime import datetime, timedelta
import time
import feedparser
import re
from twilio.rest import Client

load_dotenv()
RSS_URL = os.getenv("RSS_URL")
COURSE_CODE = os.getenv("COURSE_CODE")

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
sender_number = os.getenv("SENDER_NUMBER")
my_number = os.getenv("MY_NUMBER")

def sleep_until_next() -> None:
    now = datetime.now()
    next_run = now.replace(hour=14, minute=0, second=0, microsecond=0)

    # If it's already past 2 PM today, schedule for tomorrow
    if now >= next_run:
        next_run += timedelta(days=1)

    seconds_to_sleep = (next_run - now).total_seconds()
    print(f"Sleeping for {int(seconds_to_sleep)} seconds until next 2:00 PM.")
    time.sleep(seconds_to_sleep)

def extract_id(url: str) -> int:
    match = re.search(r'id=(\d+)', url)
    if match:
        number = match.group(1)
        return int(number)
    return None

def send_text_notification(entry) -> None:
    message = f"{entry.title} \nAuthor:{entry.author} \nLink: {entry.id}"
    client = Client(account_sid, auth_token)

    client.messages.create(
        body=message,
        from_=sender_number,
        to=my_number
    )

def check_updates() -> None:
    feed = feedparser.parse(RSS_URL)
    now = datetime.now()
    new_entries = []

    for entry in feed.entries:
        if hasattr(entry, "published_parsed"):
            entry_time = datetime.fromtimestamp(time.mktime(entry.published_parsed))
            if entry_time >= now - timedelta(days=3):
                new_entries.append(entry)

    for entry in new_entries:
        send_text_notification(entry)

while True:
    sleep_until_next()
    check_updates()
