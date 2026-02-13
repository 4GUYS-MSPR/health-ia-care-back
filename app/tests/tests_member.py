from django.urls import reverse_lazy
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
import datetime

from app.models.member import Member
from app.models.gender import Gender
from app.models.level import Level
from app.models.subscription import Subscription


class TestMember(APITestCase):
    def setUp(self):
        User = get_user_model()
        self.user_1 = User.objects.create_user(username="user_one", password="userOnePassword")
        self.user_2 = User.objects.create_user(username="user_two", password="userTwoPassword")
        self.url = reverse_lazy('member-list')
        self.gender = Gender.objects.create(value="MALE", create_at=datetime.datetime.now())
        self.level = Level.objects.create(value="BEGGINER", create_at=datetime.datetime.now())
        self.subscription = Subscription.objects.create(value="FREE", create_at=datetime.datetime.now())
     


    def test_should_return_a_list_of_members(self):
        member = Member.objects.create(
            age = 18,
            bmi = 10.5,
            fat_percentage = 18,
            height = 180,
            weight = 80.5,
            workout_frequency = 3,
            objectives = [],
            client = self.user_1,
            gender = self.gender,
            level = self.level,
            subscription = self.subscription,
            create_at = datetime.datetime.now()
        )
        Member.objects.create(
            age = 19,
            bmi = 16.5,
            fat_percentage = 20,
            height = 170,
            weight = 85.5,
            workout_frequency = 7,
            objectives = [],
            client = self.user_1,
            gender = self.gender,
            level = self.level,
            subscription = self.subscription,
            create_at = datetime.datetime.now()
        )
        Member.objects.create(
            age = 30,
            bmi = 20,
            fat_percentage = 30,
            height = 190,
            weight = 100,
            workout_frequency = 6,
            objectives = [],
            client = self.user_2,
            gender = self.gender,
            level = self.level,
            subscription = self.subscription,
            create_at = datetime.datetime.now()
        )

        self.client.force_login(self.user_1)
        self.client.force_authenticate(user=self.user_1)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        print("Le code de retour est bien 200")
        self.assertIsInstance(response.data["results"], list )
        print("L'api retourne un resultat sous forme de liste")
        self.assertEqual(len(response.data['results']),2)
        print("L'api retourne seulement les membres d'un client donné")
        
        


    def test_should_return_unauthorized_response_if_user_is_not_authentified(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 401)
        print("L'API retourne un code erreur 401")

        






