import base64
import time

def issue(user):
    raw = f"{user}:{int(time.time())}"
    return base64.b64encode(raw.encode()).decode()
