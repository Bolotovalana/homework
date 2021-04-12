import unittest

import requests

from json_parser import Coordinates


class test_json_parser(unittest.TestCase):
    def setUp(self) -> None:
        self.coord = Coordinates(35, 139)

    def tearDown(self) -> None:
        del self.coord

    def test_get_weather_data(self):
        result = self.coord.get_weather_data()
        self.assertIsInstance(result, requests.Response)

    def test_parse_json_data(self):
        example = {'coord': {'lon': 139, 'lat': 35}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': 'https://cdn.glitch.com/6e8889e5-7a72-48f0-a061-863548450de5%2F04d.png?1499366020964'}], 'base': 'stations', 'main': {'temp': 12.22, 'feels_like': 10.96, 'temp_min': 12.22, 'temp_max': 12.22, 'pressure': 1015, 'humidity': 56}, 'visibility': 10000, 'wind': {'speed': 1.34, 'deg': 103, 'gust': 5.36}, 'clouds': {'all': 98}, 'dt': 1617836309, 'sys': {'type': 3, 'id': 2019346, 'country': 'JP', 'sunrise': 1617826890, 'sunset': 1617872996}, 'timezone': 32400, 'id': 1851632, 'name': 'Shuzenji', 'cod': 200}
        result = self.coord.parse_json_data(example)
        self.assertEqual(result, "temperature=Temperature(temp=12.22, feels_like=0.0, temp_min=12.22, temp_max=54.0) "
                                 "pressure=39.960629921259844 description='overcast clouds' name='Shuzenji'")

if __name__ == '__main__':
    unittest.main()
