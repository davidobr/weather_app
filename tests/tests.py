from django.test import TestCase


class ViewsCanRenderTest(TestCase):

    def test_can_render_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)


class WeatherApiTest(TestCase):
    def test_correct_api_response(self):
        response = self.client.get('https://api.openweathermap.org/data/2.5/weather?q=Lima&appid=cc9992194592a47721720513309df459&units=metric')
        self.assertEqual(response.status_code, 200)
