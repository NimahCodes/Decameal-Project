import pytest
from django.urls import resolve, reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

pytestmark = pytest.mark.django_db

url = reverse("api:meals")


class TestUploadMealsView(APITestCase):
    def setUp(self):
        self.client = APIClient()

    def test_anonymous_user_can_view_all_meals(self):
        res = self.client.get(url, format="json")
        assert res.status_code == status.HTTP_200_OK

    def test_get_meals_url(self):
        assert reverse("api:meals") == "/api/v1/meals/"
        assert resolve("/api/v1/meals/").view_name == "api:meals"
