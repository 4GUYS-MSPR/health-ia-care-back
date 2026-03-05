from rest_framework.test import APITestCase
from rest_framework import status
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth.models import User

class TestImport(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username="admin", password="admin")
        self.client.force_authenticate(user=self.user)
        self.url = "/api/import/"

    def test_should_return_a_400_status_code_if_file_is_not_supported(self):
        invalid_content_text_file = b"Simple text file"
        mock_file = SimpleUploadedFile(
            name="test.txt",
            content=invalid_content_text_file,
            content_type="text/plain"
        )

        payload = {
            "data": mock_file,
            "classname": "MemberAction"
        }

        response = self.client.post(self.url, data=payload, format='multipart')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
