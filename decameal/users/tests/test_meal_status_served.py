import pytest
from django.urls import reverse
from rest_framework.test import APIClient, APITestCase

pytestmark = pytest.mark.django_db


class MealStatusTestSetUp(APITestCase):
    def setUp(self):
        self.client = APIClient()

    def test_meal_status_returns_forbidden_if_user_is_not_authenticated(self):
        response = self.client.get(
            reverse(
                "api:ticket-status",
                kwargs={"pk": "20f5484b-88ae-49b0-8af0-3a389b4917dd"},
            )
        )
        self.assertContains(
            response=response,
            text="Authentication credentials were not provided.",
            status_code=403,
        )
