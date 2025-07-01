from datetime import datetime
import time

def sleep_until(target_time: datetime) -> None:
    now = datetime.now()

    if now >= target_time:
        print("Target time is in the past. Skipping sleep.")
        return

    seconds_to_sleep = (target_time - now).total_seconds()
    print(f"Sleeping for {int(seconds_to_sleep)} seconds until {target_time.strftime('%Y-%m-%d %H:%M:%S')}")
    time.sleep(seconds_to_sleep)