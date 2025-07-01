from datetime import datetime
from utils.time import sleep_until
from core import check_updates

def main():
    checkup_time = datetime.now().replace(hour=5, minute=9, second=0, microsecond=0)

    while True:
        sleep_until(checkup_time)
        print("Checking updates...")
        check_updates()

if __name__ == "__main__":
    main()