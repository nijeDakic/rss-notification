from datetime import datetime, timedelta
import time
import feedparser
from models.entry import Entry
from services import send_sms
from utils.formatting import write_message
from config import Config

def check_updates() -> None:
    feed = feedparser.parse(Config.RSS_URL)
    now = datetime.now()
    new_entries: list[Entry] = []

    for entry in feed.entries:
        if hasattr(entry, "published_parsed"):
            entry_time = datetime.fromtimestamp(time.mktime(entry.published_parsed))
            if entry_time >= now - timedelta(days=3):
                new_entries.append(entry)

    for entry in new_entries:
        message = write_message(entry)
        send_sms(message)