from rest_framework.test import APITestCase
from app.tests.utils.fake_exercice import create_exercice
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
import datetime


class TestExercice(APITestCase):
    User = get_user_model()
    user_3 = User.objects.create_user(username="user_three", password="userThreePassword")
    user_4 = User.objects.create_user(username="user_four", password="userFourPassword")
    def setUp(self):
        exercie_1 = create_exercice(self.user_3)
        exercice_2 = create_exercice(self.user_3)
        exercice_3 = create_exercice(self.user_4)
        url = reverse_lazy("exercice-list")
    
    def test_should_return_status_code_200(self):
        self.client.force_login(self.user_3)
        self.client.force_authenticate(user=self.user_3)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        print("Le code de retour est bien 200")
