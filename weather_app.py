import requests

API_KEY = "your_openweather_api_key"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        weather = data['weather'][0]['description']
        return f"{city.title()}: {temp}°C, {weather}"
    else:
        return "City not found."

if __name__ == "__main__":
    city = input("Enter city name: ")
    print(get_weather(city))
