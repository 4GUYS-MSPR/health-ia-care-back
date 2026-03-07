from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model

class TestToken(APITestCase):
    def setUp(self):
        User = get_user_model()
        self.url = "/api/token/"
        self.user_1 = User.objects.create_user(username = "Test", password = "Password")

    def test_should_return_a_token(self):
        data = {"username": "Test", "password": "Password"}
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.data["token"], str)
        self.assertIn("token", response.data)

    def test_should_return_an_error_if_password_doesnt_match(self):
        data = {"username": "Test", "password": "Password2"}
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, 400)
