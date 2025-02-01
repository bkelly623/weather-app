import requests
import os

API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL_CURRENT = "http://api.openweathermap.org/data/2.5/weather"
BASE_URL_FORECAST = "https://api.openweathermap.org/data/2.5/onecall"

def get_weather(city):
    # Get current weather data
    params = {"q": city, "appid": API_KEY, "units": "imperial"}
    response = requests.get(BASE_URL_CURRENT, params=params)
    data = response.json()

    if response.status_code == 200:
        lat = data["coord"]["lat"]
        lon = data["coord"]["lon"]
        weather = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]

        print(f"\nCurrent Weather in {city}:")
        print(f"  Condition: {weather.capitalize()}")
        print(f"  Temperature: {temp}°F (Feels like {feels_like}°F)")
        print(f"  Humidity: {humidity}%")

        # Fetch 7-day forecast
        get_forecast(lat, lon)

    else:
        print("City not found or API error.")

def get_forecast(lat, lon):
    params = {
        "lat": lat,
        "lon": lon,
        "appid": API_KEY,
        "exclude": "current,minutely,hourly,alerts",
        "units": "imperial"
    }
    response = requests.get(BASE_URL_FORECAST, params=params)
    data = response.json()

    if response.status_code == 200:
        print("\n7-Day Forecast:")
        for day in data["daily"]:
            temp_day = day["temp"]["day"]
            temp_night = day["temp"]["night"]
            condition = day["weather"][0]["description"]
            print(f"  {condition.capitalize()}, Day: {temp_day}°F, Night: {temp_night}°F")

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)
