import requests
import time

def get(url, timeout=3):
    start = time.time()
    try:
        r = requests.get(url, timeout=timeout)
        latency = (time.time() - start) * 1000
        return r, latency
    except Exception:
        return None, None
