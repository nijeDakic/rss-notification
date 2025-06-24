from dotenv import load_dotenv
import os
import datetime
import feedparser
from twilio.rest import Client

load_dotenv()

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
sender_number = os.getenv("SENDER_NUMBER")
my_number = os.getenv("MY_NUMBER")

RSS_URL = os.getenv("RSS_URL")
COURSE_CODE = os.getenv("COURSE_CODE")

# fix sending all blogs
def send_text_notification(blogs: list):
    client = Client(account_sid, auth_token)

    for blog in blogs: 
        client.messages.create(
            body="Razvalio si kola, bolje vozi sledeci put",
            from_=sender_number,
            to=my_number
        )

# get all rss news
def check_updates():
    send_text_notification()


feed = feedparser.parse(RSS_URL)

print(feed.entries[0].published_parsed)
# print("Entry Title:", feed.entries[0].title)
# print("Entry Published Date:", feed.entries[0].published)
# print("Entry Summary:", feed.entries[0].summary)

# while True:
#     current_time = time.localtime()
#     if current_time.tm_hour == 2 and current_time.tm_min == 0 and current_time.tm_sec == 0:
#         check_updates()
#     time.sleep(3600*24-10)
#     break

