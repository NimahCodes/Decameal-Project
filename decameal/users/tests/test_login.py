import pytest
from django.urls import resolve, reverse
from rest_framework.test import APIClient, APITestCase

from ..models import User

pytestmark = pytest.mark.django_db
LOGIN_URL = reverse("api:login")
REGISTER_URL = reverse("api:register")


class TestLogin(APITestCase):
    def test_login_url(self):
        assert reverse("api:login") == "/api/v1/auth/login/"
        assert resolve("/api/v1/auth/login/").view_name == "api:login"

    def test_login_endpoint_with_verified_user(self):
        payload = {
            "email": "test@decagon.dev",
            "username": "tester",
            "first_name": "test",
            "last_name": "testingangle",
            "mobile_number": "080419419",
            "password": "testingun",
            "role": "Decadev",
        }
        client = APIClient()
        client.post(REGISTER_URL, payload)
        user = User.objects.get(email="test@decagon.dev")
        user.is_verified = True
        user.save()
        res = client.post(
            LOGIN_URL, {"email": "test@decagon.dev", "password": "testingun"}
        )
        assert res.status_code == 200

    def test_login_endpoint_without_user_verification(self):
        payload = {
            "email": "test@decagon.dev",
            "username": "tester",
            "first_name": "test",
            "last_name": "testingangle",
            "mobile_number": "080419419",
            "password": "testingun",
            "role": "Decadev",
        }
        client = APIClient()
        client.post(REGISTER_URL, payload)
        res = client.post(
            LOGIN_URL, {"email": "test@decagon.dev", "password": "testingun"}
        )
        assert res.status_code == 400

    def test_login_endpoint_with_wrong_email(self):
        payload = {
            "email": "test@decagon.dev",
            "username": "tester",
            "first_name": "test",
            "last_name": "testingangle",
            "mobile_number": "080419419",
            "password": "testingun",
            "role": "Decadev",
        }
        client = APIClient()
        client.post(REGISTER_URL, payload)
        user = User.objects.get(email="test@decagon.dev")
        user.is_verified = True
        user.save()
        res = client.post(
            LOGIN_URL, {"email": "test@coding.dev", "password": "testingun"}
        )
        assert res.status_code == 400

    def test_login_endpoint_with_wrong_password(self):
        payload = {
            "email": "test@decagon.dev",
            "username": "tester",
            "first_name": "test",
            "last_name": "testingangle",
            "mobile_number": "080419419",
            "password": "testingun",
            "role": "Decadev",
        }
        client = APIClient()
        client.post(REGISTER_URL, payload)
        user = User.objects.get(email="test@decagon.dev")
        user.is_verified = True
        user.save()
        res = client.post(
            LOGIN_URL, {"email": "test@decagon.dev", "password": "testing"}
        )
        assert res.status_code == 400

    def test_login_endpoint_with_unregistered_user(self):
        client = APIClient()
        res = client.post(
            LOGIN_URL, {"email": "test@decagon.dev", "password": "testing"}
        )
        assert res.status_code == 400
