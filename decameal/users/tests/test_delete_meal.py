from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from decameal.users.api.models.meal import Meal
from decameal.users.api.models.meal_category import MealCategory


class TestSetup(APITestCase):
    def setUp(self):
        self.mealcategory = MealCategory.objects.create(
            name="Rice",
        )
        self.meal = Meal.objects.create(
            title="Food rice",
            description="The food is working",
            cover_img="https://images.app.goo.gl/Zqz5fjVVLR6dLD5p9",
            category_id=self.mealcategory,
        )
        self.delete_meal_url = reverse("api:meals", kwargs={"pk": self.meal.pk})

    def test_delete_meal_that_does_not_exist(self):
        res = self.client.delete(self.delete_meal_url, format="json")
        try:
            Meal.objects.get(
                title="Beans",
            )
        except ObjectDoesNotExist:
            self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

        self.assertEqual(res.status_code, 403)
