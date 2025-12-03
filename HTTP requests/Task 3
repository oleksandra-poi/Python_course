import requests

api_key = "YOUR_API_KEY"
city = input("Choose the city: ")
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)
data = response.json()
print(data['weather'][0]['description'])
print(data['main']['temp'], "°C")
print("Feels like:", data['main']['feels_like'], "°C")
