import pytest
from django.urls import resolve, reverse
from rest_framework.test import APITestCase

pytestmark = pytest.mark.django_db

register_url = reverse("api:reset")


class TestUser(APITestCase):
    def test_reset_password_url(self):
        assert reverse("api:reset") == "/api/v1/auth/reset-password/"
        assert resolve("/api/v1/auth/reset-password/").view_name == "api:reset"
