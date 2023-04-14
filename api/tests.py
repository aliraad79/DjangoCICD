from django.test import TestCase, Client


class ApiTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_api_health(self):
        response = self.client.get("/api/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b"Hello, world. You're at the index.")

    def test_greeting(self):
        response = self.client.get("/api/greet/ali/22/")
        self.assertLess(response.status_code, 400)
        self.assertEqual(response.content, b"Hello, ali. You're 22 years old.")
