import pytest
from django.urls import resolve, reverse
from rest_framework.test import APITestCase

pytestmark = pytest.mark.django_db

forgot_password_url = reverse("api:forgot")


class TestUser(APITestCase):
    def test_forgot_password_url(self):
        assert reverse("api:forgot") == "/api/v1/auth/forgot-password/"
        assert resolve("/api/v1/auth/forgot-password/").view_name == "api:forgot"
