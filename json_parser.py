import requests
import json
from pydantic import BaseModel, validator


class Temperature(BaseModel):
    temp: float
    feels_like: float = None
    temp_min: float
    temp_max: float

    """
    convert celsius value to fahrenheit
    """

    @validator('temp')
    def celsius_to_fahrenheit(cls, value: float) -> float:
        return round(value * 9 / 5 + 32, 2)


class Weather(BaseModel):
    temperature: Temperature
    pressure: int
    description: str
    name: str

    """
    convert getting mmHG value to inHG
    """

    @validator('pressure')
    def mmhg_to_inhg(cls, value: int) -> float:
        return value / 25.4


class Coordinates:
    def __init__(self, longitude: int, latitude: int):
        self.longitude = longitude
        self.latitude = latitude

    def get_weather_data(self):
        """
        send GET http requests on the server and return JSON response"
        """
        link = f"https://fcc-weather-api.glitch.me/api/current?lat={self.longitude}&lon={self.latitude}"
        result = requests.get(link)
        return result

    def parse_json_data(self, json_data):
        """
        Get JSON response and retrieve certain parameters from JSON and return object Weather with schema data

        """
        j_data = json.loads(json_data.text)
        try:
            feels_like = j_data.get['main']['feels_like']
        except:
            feels_like = 0
        data = {
            'temperature': {
                'temp': j_data['main']['temp'],
                'feels_like': feels_like,
                'temp_min': j_data['main']['temp_min'],
                'temp_max': j_data['main']['temp_max']
            },
            'description': j_data['weather'][0]['description'],
            'pressure': j_data['main']['pressure'],
            'name': j_data['name']
        }
        return Weather(**data)


coordinates = Coordinates(35, 139)
json_data = coordinates.get_weather_data()
weather = coordinates.parse_json_data(json_data)
print(f"Current weather in {weather.name}: {weather.description}, temperature is {weather.temperature.temp}F \n"
      f"feels_like is {weather.temperature.feels_like}F, minimal temperature is {weather.temperature.temp_min}F, \n"
      f"maximum temperature is {weather.temperature.temp_max}F, pressure is {weather.pressure}")
