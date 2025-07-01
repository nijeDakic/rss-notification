import re

def extract_id(url: str) -> int:
    match = re.search(r'id=(\d+)', url)
    if match:
        number = match.group(1)
        return int(number)
    return None