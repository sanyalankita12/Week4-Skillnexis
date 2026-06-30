import requests
import os
from dotenv import load_dotenv

# Load API key
load_dotenv()
API_KEY = os.getenv("API_KEY")

# Get city name
city = input("Enter city name: ")

# API URL
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

# Send request
response = requests.get(url)

# Check response
if response.status_code == 200:
    data = response.json()

    print("\n------ Weather Report ------")
    print("City:", data["name"])
    print("Country:", data["sys"]["country"])
    print("Temperature:", data["main"]["temp"], "°C")
    print("Humidity:", data["main"]["humidity"], "%")
    print("Weather:", data["weather"][0]["description"])
    print("----------------------------")

else:
    print("City not found or Invalid API Key.")