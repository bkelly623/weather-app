import requests
import os

API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if response.status_code == 200:
        weather = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        print(f"Weather in {city}: {weather.capitalize()}")
        print(f"Temperature: {temp}°C (Feels like {feels_like}°C)")
        print(f"Humidity: {humidity}%")
    else:
        print("City not found or API error.")

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)
