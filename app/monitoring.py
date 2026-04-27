import requests
import time

URL = "https://api.open-meteo.com/v1/forecast?latitude=48.85&longitude=2.35&current_weather=true"

latencies = []

for i in range(5):
    start = time.time()
    r = requests.get(URL)
    latencies.append(time.time() - start)

print("📊 Moyenne :", sum(latencies) / len(latencies))
print("📊 Min :", min(latencies))
print("📊 Max :", max(latencies))

if all(r.status_code == 200 for _ in range(5)):
    print("🟢 API stable")
else:
    print("🔴 API instable")
