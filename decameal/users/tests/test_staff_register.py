import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

pytestmark = pytest.mark.django_db

register_url = reverse("api:register_staff")


class TestUser(APITestCase):
    def setUp(self):

        self.client = APIClient()

    def test_create_valid_staff_user_success(self):
        payload = {
            "email": "test@decagon.dev",
            "username": "tester",
            "first_name": "test",
            "last_name": "testingangle",
            "mobile_number": "080419419",
            "password": "testingun",
            "role": "Staff",
        }
        res = self.client.post(register_url, payload)
        assert res.status_code == status.HTTP_200_OK

    def test_no_username(self):
        payload = {
            "email": "test@decagon.dev",
            "first_name": "test",
            "last_name": "testingangle",
            "mobile_number": "080419419",
            "password": "testingun",
            "role": "Dev",
        }
        res = self.client.post(register_url, payload)
        assert res.status_code == status.HTTP_400_BAD_REQUEST

    def test_registration_with_missing_fields(self):
        payload = {
            "email": "test@decagon.dev",
            "last_name": "testingangle",
            "mobile_number": "080419419",
            "password": "testingun",
        }
        res = self.client.post(register_url, payload)
        assert res.status_code == status.HTTP_400_BAD_REQUEST
