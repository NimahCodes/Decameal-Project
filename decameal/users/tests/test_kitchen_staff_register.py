import pytest

from .test_setup import TestSetup

pytestmark = pytest.mark.django_db


class TestView(TestSetup):
    def test_user_cannot_register_with_no_data(self):
        res = self.client.post(self.register_url)
        assert res.status_code == 400

    def test_user_can_register(self):
        payload = {
            "email": "test@decagon.dev",
            "username": "tester",
            "first_name": "test",
            "last_name": "testingangle",
            "mobile_number": "080419419",
            "password": "testingun",
        }
        res = self.client.post(self.register_url, payload, format="json")
        assert res.status_code == 200
