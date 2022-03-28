import pytest
from django.test import Client
from django.urls import resolve, reverse

pytestmark = pytest.mark.django_db

VERIFY_URL = reverse("api:verify")
REGISTER_URL = reverse("api:register")


class TestEmailVerification:
    def test_verification_url(self):
        assert reverse("api:verify") == "/api/v1/auth/verify/"
        assert resolve("/api/v1/auth/verify/").view_name == "api:verify"

    def test_email_verification_with_wrong_otp(self):
        client = Client()
        res = client.post(VERIFY_URL, email="test@test.com", otp="123490")
        assert res.status_code == 400
