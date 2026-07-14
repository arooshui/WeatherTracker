import os
import requests
from dotenv import load_dotenv
from utils.logger import logger

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")


def get_weather(city):

    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}"

    try:

        logger.info(f"Fetching weather data for city: {city}")

        response = requests.get(url)

        response.raise_for_status()

        data = response.json()

        weather = {
            "city": data["location"]["name"],
            "country": data["location"]["country"],
            "latitude": data["location"]["lat"],
            "longitude": data["location"]["lon"],
            "temperature": data["current"]["temp_c"],
            "humidity": data["current"]["humidity"],
            "pressure": data["current"]["pressure_mb"],
            "wind_speed": data["current"]["wind_kph"],
            "weather_condition": data["current"]["condition"]["text"],
            "fetched_at": data["location"]["localtime"]
        }

        logger.info(f"Weather data fetched successfully for city: {city}")

        return weather

    except requests.exceptions.RequestException as e:

        logger.exception(f"Failed to fetch weather data for city: {city}")

        return None