from twilio.rest import Client
from config import Config
from utils import write_message
from models import Entry

def send_notification(entry: Entry) -> None:
    message = write_message(entry)
    client = Client(Config.account_sid, Config.auth_token)

    client.messages.create(
        body=message,
        from_=Config.sender_number,
        to=Config.my_number
    )