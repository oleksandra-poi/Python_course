import requests
import threading
import json

urls = [
    "https://jsonplaceholder.typicode.com/comments"
]

all_results = []
def receive_data(url):
    response = requests.get(url)
    data = response.json()
    all_results.append(data)

threads = []
for url in urls:
    thread = threading.Thread(target=receive_data, args=(url,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(all_results, f, indent=4, ensure_ascii=False)

print("Done!")
