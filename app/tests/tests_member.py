from rest_framework.test import APITestCase
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from app.tests.utils.fake_member import create_member

class TestMember(APITestCase):
    def setUp(self):
        User = get_user_model()
        self.user_1 = User.objects.create_user(username="user_one", password="userOnePassword")
        self.user_2 = User.objects.create_user(username="user_two", password="userTwoPassword")
        self.url = reverse_lazy('member-list')
        self.member_1 = create_member(self.user_1)
        self.member_2 = create_member(self.user_1)
        self.member_3 = create_member(self.user_2)

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
