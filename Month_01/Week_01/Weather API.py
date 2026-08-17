import os

import requests
from dotenv import load_dotenv


GEOCODING_URL = "https://api.openweathermap.org/geo/1.0/direct"
CURRENT_WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"
FORECAST_URL = "https://api.openweathermap.org/data/2.5/forecast"

load_dotenv()
API_KEY = os.getenv("API_KEY")


def get_coordinates(city_name):
    try:
        response = requests.get(
            GEOCODING_URL,
            params={"q": city_name, "limit": 1, "appid": API_KEY},
            timeout=10,
        )
        response.raise_for_status()
        locations = response.json()
    except requests.RequestException as error:
        print(f"Could not find the city: {error}")
        return None, None

    if not locations:
        print("City not found. Try a city and country code, for example: Islamabad,PK")
        return None, None

    return locations[0]["lat"], locations[0]["lon"]


def get_weather(lat, lon):
    try:
        response = requests.get(
            CURRENT_WEATHER_URL,
            params={
                "lat": lat,
                "lon": lon,
                "appid": API_KEY,
                "units": "metric",
            },
            timeout=10,
        )
        response.raise_for_status()
        return response.json()
    except requests.RequestException as error:
        print(f"Could not fetch current weather: {error}")
        return None


def get_forecast(lat, lon):
    try:
        response = requests.get(
            FORECAST_URL,
            params={
                "lat": lat,
                "lon": lon,
                "appid": API_KEY,
                "units": "metric",
            },
            timeout=10,
        )
        response.raise_for_status()
        return response.json()
    except requests.RequestException as error:
        print(f"Could not fetch forecast: {error}")
        return None


def display_weather(city_name, current_data, forecast_data):
    print(f"\nWeather in {city_name.title()}:")
    print(f"Temperature: {current_data['main']['temp']}°C")
    print(f"Weather: {current_data['weather'][0]['description']}")
    print(f"Humidity: {current_data['main']['humidity']}%")
    print(f"Wind speed: {current_data['wind']['speed']} m/s")

    print("\nForecast:")
    for item in forecast_data["list"][:5]:
        print(
            f"{item['dt_txt']}: {item['main']['temp']}°C, "
            f"{item['weather'][0]['description']}"
        )


def main():
    if not API_KEY:
        print("API_KEY is missing. Add it to your .env file and try again.")
        return

    while True:
        city_name = input("\nEnter a city name (or 'q' to quit): ").strip()

        if city_name.casefold() == "q":
            print("Goodbye!")
            break

        if not city_name:
            print("City name cannot be empty.")
            continue

        lat, lon = get_coordinates(city_name)
        if lat is None or lon is None:
            continue

        current_data = get_weather(lat, lon)
        forecast_data = get_forecast(lat, lon)
        if current_data is None or forecast_data is None:
            continue

        display_weather(city_name, current_data, forecast_data)


if __name__ == "__main__":
    main()
