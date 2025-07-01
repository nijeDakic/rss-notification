from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    RSS_URL = os.getenv("RSS_URL")
    COURSE_CODE = os.getenv("COURSE_CODE")

    account_sid = os.getenv("TWILIO_ACCOUNT_SID")
    auth_token = os.getenv("TWILIO_AUTH_TOKEN")
    sender_number = os.getenv("SENDER_NUMBER")
    my_number = os.getenv("MY_NUMBER")