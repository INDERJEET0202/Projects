from pydoc import tempfilepager
from urllib import response
import requests

API_KEY = "e92890feea239e7f26c9e30d30da3a18"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?q={city}&appid={API_KEY}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    # print(data)
    weather = data['weather'][0]['description']
    temperature = round(data['main']['temp'] - 273.15, 2)
    min_temp = round(data['main']['temp_min'] - 273.15, 2)
    max_temp = round(data['main']['temp_max'] - 273.15, 2)
    winds = data['wind']['speed']
    humidity = data['main']['humidity']
    # rain = data['rain']['3h']
    # uv_index = data['uvi']
    clouds = data['clouds']['all']
    #sunrise in hours
    sunrise = data['sys']['sunrise']
    sunrise_hour = sunrise // 3600
    sunset = data['sys']['sunset']
    sunset_hour = sunset // 3600
    name = data['name']
    country = data['sys']['country']
    pressure = data['main']['pressure']
    visibility = data['visibility']
    print(f" Name: {name}\n Country: {country}\n Weather: {weather}\n Temperature: {temperature}\n Min Temperature: {min_temp}\n Max Temperature: {max_temp}\n Winds: {winds}\n Humidity: {humidity}\n Clouds: {clouds}\n Sunrise: {sunrise_hour}\n Sunset: {sunset_hour}\n Pressure: {pressure}\n Visibility: {visibility}\n")

else:
    print("Error occurred!")