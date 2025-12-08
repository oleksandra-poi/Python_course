#-------------------1st request--------------------
import requests

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)
data = response.json()

for user in data[:5]:
    print(user['name'])

print("HTTP status code: ", response.status_code)


#--------------------2nd request---------------------
import requests

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)
users = response.json()

for user in users:
    if user['email'] == 'Shanna@melissa.tv':
        print(user)

print("HTTP status code: ", response.status_code)


#---------------------3rd request----------------------
import requests

url = "https://jsonplaceholder.typicode.com/posts"

inf =  {
  "title": "My test post",
  "body": "Hello from Python!",
  "userId": 1
}

response = requests.post(url, json=inf)
data = response.json()
print("Server response:", data)

if response.status_code == 201:
    print("Information was successfully added!")
else:
    print("Failed to add information. Status code:", response.status_code)


#------------------------4th request---------------------
import requests

url = "https://jsonplaceholder.typicode.com/posts/5"

response = requests.delete(url)

if response.status_code == 200 or response.status_code == 204:
    print("Deleted")
else:
    print("Not deleted. Status code:", response.status_code)
