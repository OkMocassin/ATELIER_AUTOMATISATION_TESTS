import requests
import time

URL = "https://api.open-meteo.com/v1/forecast?latitude=48.85&longitude=2.35&current_weather=true"

def test_api():
    start = time.time()

    r = requests.get(URL, timeout=5)
    latency = time.time() - start

    if r.status_code == 200:
        data = r.json()

        print("✅ API OK")
        print("⏱ Latence :", round(latency, 2), "sec")

        return {
            "status": "OK",
            "latency": latency
        }
    else:
        print("❌ API FAIL")
        return {"status": "FAIL"}

test_api()
