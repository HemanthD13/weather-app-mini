# modules/api_handler.py
import requests
from config import API_KEY


def fetch_weather_data(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise error for invalid responses
        data = response.json()

        # Extract relevant data
        weather = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "weather_description": data["weather"][0]["description"],
            "wind_speed": data["wind"]["speed"],
        }

        return weather
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None
