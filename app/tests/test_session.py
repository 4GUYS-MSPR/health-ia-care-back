# import datetime
# from datetime import time
# from rest_framework.test import APITestCase
# from django.urls import reverse_lazy
# from django.contrib.auth import get_user_model

# from app.models.session import Session
# from app.serializers.session import SessionSerializer
# from app.tests.utils.fake_member import create_member
# from app.tests.utils.fake_exercice import create_exercice

# class TestSession(APITestCase):
#     def setUp(self):
#         User = get_user_model()
#         self.user_1 = User.objects.create_user(username="user_one", password="userOnePassword")
#         self.user_2 = User.objects.create_user(username="user_two", password="userTwoPassword")
#         self.url = reverse_lazy('session-list')
#         self.member_1 = create_member(self.user_2, self.user_1)
#         self.exercice_1 = create_exercice(self.user_1)
#         session_1 = Session.objects.create(
#             avg_bpm = 12,
#             calories_burned = 20.5,
#             duration = datetime.time(),
#             max_bpm = 180,
#             resting_bpm = 60,
#             water_intake = 1.5,
#             client = self.user_1,
#             member =self.member_1,
#             create_at = datetime.datetime.now()
#         )
#         session_2 = Session.objects.create(
#             avg_bpm = 12,
#             calories_burned = 20.5,
#             duration = datetime.time(),
#             max_bpm = 180,
#             resting_bpm = 60,
#             water_intake = 1.5,
#             client = self.user_2,
#             member =self.member_1,
#             create_at = datetime.datetime.now()
#         )
#         session_3 = Session.objects.create(
#             avg_bpm = 12,
#             calories_burned = 20.5,
#             duration = datetime.time(),
#             max_bpm = 180,
#             resting_bpm = 60,
#             water_intake = 1.5,
#             client = self.user_2,
#             member =self.member_1,
#             create_at = datetime.datetime.now()
#         )
#         self.session_4 = Session.objects.create(
#             avg_bpm = 12,
#             calories_burned = 20.5,
#             duration = time(1, 30),
#             max_bpm = 180,
#             resting_bpm = 60,
#             water_intake = 1.5,
#             client = self.user_2,
#             member =self.member_1,
#             create_at = datetime.datetime.now()
#         )

#         session_1.exercices.set([self.exercice_1])
#         session_2.exercices.set([self.exercice_1])
#         session_3.exercices.set([self.exercice_1])
#         self.session_4.exercices.set([self.exercice_1])

#         self.serializer = SessionSerializer(instance=self.session_4)

#     def test_should_return_a_list_of_session(self):
#         self.client.force_login(self.user_1)
#         self.client.force_authenticate(user=self.user_1)
#         response = self.client.get(self.url)
#         self.assertEqual(response.status_code, 200)
#         print("Le code de retour est bien 200")
#         self.assertIsInstance(response.data["results"], list )
#         print("L'api retourne un resultat sous forme de liste")

#     def test_should_return_only_personal_session(self):
#         self.client.force_login(self.user_2)
#         self.client.force_authenticate(user=self.user_2)
#         response = self.client.get(self.url)
#         self.assertEqual(len(response.data["results"]), 3)
#         print("La liste retourne uniquement les sessions d'un client donné ")

#     def test_should_return_unauthorized_response_if_user_is_not_authentified(self):
#         response = self.client.get(self.url)
#         self.assertEqual(response.status_code, 401)
#         print("L'API retourne un code erreur 401")

#     def test_response_should_match_with_session_serializer(self):
#         data = self.serializer.data
#         self.assertEqual(data['id'], self.session_4.id)
#         self.assertEqual(data['avg_bpm'], 12)
#         self.assertEqual(data['calories_burned'], 20.5)
#         self.assertEqual(data['duration'], "01:30:00")
#         self.assertEqual(data['max_bpm'], 180)
#         self.assertEqual(data['resting_bpm'], 60)
#         self.assertEqual(data['water_intake'], 1.5)
#         self.assertEqual(data['member'], self.member_1.id)

#     def test_response_should_match_with_type_of_serializer(self):
#         data = self.serializer.data
#         self.assertIsInstance(data['id'], int)
#         self.assertIsInstance(data['avg_bpm'], int)
#         self.assertIsInstance(data['calories_burned'], float)
#         self.assertIsInstance(data['duration'], str)
#         self.assertIsInstance(data['max_bpm'], int)
#         self.assertIsInstance(data['resting_bpm'], int)
#         self.assertIsInstance(data['water_intake'], float)
#         self.assertIsInstance(data['member'], int)
