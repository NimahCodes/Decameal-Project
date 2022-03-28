import pytest
from django.contrib.auth import get_user_model
from django.urls import resolve, reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from decameal.users.api.models.meal_category import MealCategory

pytestmark = pytest.mark.django_db

url = reverse("api:meals")


class TestUploadMealsView(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.meal_category = MealCategory.objects.create(name="test_category")
        self.user = get_user_model().objects.create(
            email="jdoe@gmail.com", username="testname", password="testpassword123"
        )
        self.user.set_password("testpassword123")
        self.user.save()

    def test_anonymous_user_cannot_upload_meal(self):
        payload = {
            "title": "test_meal",
            "description": "test_description",
            "category_id": self.meal_category.id,
            "cover_img": "test.png",
        }
        res = self.client.post(url, payload, format="json")
        assert res.status_code == status.HTTP_403_FORBIDDEN

    def test_decadev_cannot_upload_meal(self):
        self.user.role = "Decadev"
        self.user.save()
        self.client.force_authenticate(user=self.user)
        payload = {
            "title": "test_meal",
            "description": "test_description",
            "category_id": self.meal_category.id,
            "cover_img": "test.png",
        }
        res = self.client.post(url, payload, user=self.user)
        assert res.status_code == status.HTTP_403_FORBIDDEN

    def test_staff_cannot_upload_meal(self):
        self.user.role = "Staff"
        self.user.save()
        self.client.force_authenticate(user=self.user)
        payload = {
            "title": "test_meal",
            "description": "test_description",
            "category_id": self.meal_category.id,
            "cover_img": "test.png",
        }
        res = self.client.post(url, payload, user=self.user)
        assert res.status_code == status.HTTP_403_FORBIDDEN

    def test_upload_meal_url(self):
        assert reverse("api:meals") == "/api/v1/meals/"
        assert resolve("/api/v1/meals/").view_name == "api:meals"
