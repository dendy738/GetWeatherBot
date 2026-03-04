import unittest
import requests


class TestGetWeather(unittest.TestCase):
    def test_response_200(self):
        cities = ('canada', 'new York', 'California', 'camBodGia')

        status_codes = []
        expected = {200}

        for city in cities:
            response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city.title()}&appid=e90fab7014064d2c88795d9fd95afa6f')
            status_codes.append(response.status_code)

        self.assertEqual(set(status_codes), expected)

    def test_response_404(self):
        cities = ('GGWP', 'HND', 'Hallelujah')
        expected = {404}

        status_codes = []
        for city in cities:
            response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city.title()}&appid=e90fab7014064d2c88795d9fd95afa6f')
            status_codes.append(response.status_code)

        self.assertEqual(set(status_codes), expected)






