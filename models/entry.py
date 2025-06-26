from utils import extract_id
import datetime

class Entry:
    def __init__(self, rss_entry):
        self.id = extract_id(rss_entry.id)
        self.title = rss_entry.title
        self.link = rss_entry.link
        self.author = rss_entry.author
        self.date = datetime.fromisoformat(rss_entry.published)
        self.summary = rss_entry.summary
    
