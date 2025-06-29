import requests
import json

url = "https://remoteok.com/api"
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)
data = response.json()

# The first item is metadata, skip it
jobs = data[1:]

with open("jobs.json", "w", encoding="utf-8") as f:
    json.dump(jobs, f, indent=2)

print(f"✅ Data saved to jobs.json with {len(jobs)} jobs.")
