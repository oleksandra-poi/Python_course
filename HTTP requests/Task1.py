import requests
url = "https://www.twitter.com/robots.txt"
response = requests.get(url)

with open("twitter_robots.txt", "w", encoding="utf-8") as file:
    file.write(response.text)
