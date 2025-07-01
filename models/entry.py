from utils import extract_id
import datetime

class Entry:
    def __init__(self, rss_entry):
        self.id: int = extract_id(rss_entry.id)
        self.title: str = rss_entry.title
        self.link: str = rss_entry.link
        self.author: str = rss_entry.author
        self.date: datetime = datetime.fromisoformat(rss_entry.published)
        self.summary: str = rss_entry.summary
    
