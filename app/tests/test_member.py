from rest_framework.test import APITestCase
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from app.tests.utils.fake_member import create_member
from app.serializers.member import MemberSerializer

class TestMember(APITestCase):
    def setUp(self):
        User = get_user_model()
        self.user_1 = User.objects.create_user(username="user_one", password="userOnePassword")
        self.user_2 = User.objects.create_user(username="user_two", password="userTwoPassword")
        self.url = reverse_lazy('member-list')
        self.member_1 = create_member(self.user_1)
        self.member_2 = create_member(self.user_1)
        self.member_4 = create_member(self.user_2)

        self.serializer = MemberSerializer(instance=self.member_4)

    def test_should_return_a_list_of_members(self):
        self.client.force_login(self.user_1)
        self.client.force_authenticate(user=self.user_1)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        print("Le code de retour est bien 200")
        self.assertIsInstance(response.data["results"], list )
        print("L'api retourne un resultat sous forme de liste")

    def test_should_return_unauthorized_response_if_user_is_not_authentified(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 401)
        print("L'API retourne un code erreur 401")

    def test_should_return_only_member_of_logged_client(self):
        self.client.force_login(self.user_1)
        self.client.force_authenticate(user=self.user_1)
        response = self.client.get(self.url)
        self.assertEqual(len(response.data['results']),2)
        print("L'api retourne seulement les membres d'un client donné")

    def test_response_should_match_with_member_serializer(self):
        data = self.serializer.data
        self.assertEqual(data['id'], self.member_4.id)
        self.assertEqual(data['age'], 18)
        self.assertEqual(data['bmi'], 10.5)
        self.assertEqual(data['fat_percentage'], 18.2)
        self.assertEqual(data['height'], 180.2)
        self.assertEqual(data['weight'], 80.5)
        self.assertEqual(data['workout_frequency'], 3)
        self.assertEqual(data['objectives'], [])
        self.assertEqual(data['gender']['value'], "FEMALE" )
        self.assertEqual(data['level']['value'], "BEGINNER" )
        self.assertEqual(data['subscription']['value'], "FREE" )

    def test_response_should_match_with_member_serializer_type(self):
        data = self.serializer.data
        self.assertIsInstance(data['id'], int)
        self.assertIsInstance(data['age'], int)
        self.assertIsInstance(data['bmi'], float)
        self.assertIsInstance(data['fat_percentage'], float)
        self.assertIsInstance(data['height'], float)
        self.assertIsInstance(data['weight'], float)
        self.assertIsInstance(data['workout_frequency'], int)
        self.assertIsInstance(data['objectives'], list)
        self.assertIsInstance(data['gender'], dict)
        self.assertIsInstance(data['level'], dict)
        self.assertIsInstance(data['subscription'], dict)
