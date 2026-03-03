import datetime
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from app.tests.utils.fake_exercice import create_exercice
from app.serializers.exercice import ExerciceSerializer

class TestExercice(APITestCase):
    
    def setUp(self):
        User = get_user_model()
        self.user_3 = User.objects.create_user(username="user_three", password="userThreePassword")
        self.user_4 = User.objects.create_user(username="user_four", password="userFourPassword")
        self.exercice_1 = create_exercice(self.user_3)
        self.exercice_2 = create_exercice(self.user_3)
        self.exercice_3 = create_exercice(self.user_4)
        self.url = reverse_lazy("exercice-list")
        self.serializer = ExerciceSerializer(instance=self.exercice_1)

    def force_auth(self):
        """
            Function to login a user
        """
        self.client.force_login(self.user_3)
        self.client.force_authenticate(user=self.user_3)

    def test_should_return_status_code_200(self):
        self.force_auth()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        print("Le code de retour est bien 200")
    
    def test_should_return_a_list_of_exercices(self):
        self.force_auth()
        response = self.client.get(self.url)
        self.assertIsInstance(response.data['results'], list)
        print("L'API retourne les résultats dans une liste")

    def test_should_return_two_exercices(self):
        self.force_auth()
        response = self.client.get(self.url)
        self.assertEqual(len(response.data['results']), 2)
        print("L'API retourne une liste de 2 éléments")

    def test_should_return_unauthorized_response(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 401)
        print("L'API n'autorise pas l'appel sur la route")

    def test_response_should_match_to_serializer(self):
        data = self.serializer.data
        self.assertEqual(data["id"], self.exercice_1.id)
        self.assertEqual(data["image_url"], "https://image.com")
        self.assertEqual(data["category"]["value"], "YOGA")
        self.assertEqual(data["client"], self.user_3.id)
        self.assertEqual(data["body_parts"][0]["value"], "FACE")
        self.assertEqual(data["equipments"][0]["value"], "STICK")
        self.assertEqual(data["secondary_muscles"][0]["value"], "SPLENIUS")
        self.assertEqual(data["target_muscles"][0]["value"], "SPLENIUS")
        
    def test_response_should_match_with_serializer_type(self):
        data = self.serializer.data
        self.assertIsInstance(data["id"], int)
        self.assertIsInstance(data["image_url"], str)
        self.assertIsInstance(data["category"]["value"], str)
        self.assertIsInstance(data["client"], int)
        self.assertIsInstance(data["body_parts"][0]["value"], str)
        self.assertIsInstance(data["equipments"][0]["value"], str)
        self.assertIsInstance(data["secondary_muscles"][0]["value"], str)
        self.assertIsInstance(data["target_muscles"][0]["value"], str)







        

        