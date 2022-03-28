import uuid

from django.db import models

from .meal_category import MealCategory


class Meal(models.Model):
    DEFAULT_AVATAR_URL = "https://res.cloudinary.com/decameal/image/upload/v1645016151/MealThumbnails/food_c1rmga.png"
    id = models.UUIDField(
        primary_key=True, unique=True, default=uuid.uuid4, editable=False
    )
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    cover_img = models.URLField(default=DEFAULT_AVATAR_URL)
    category_id = models.ForeignKey(MealCategory, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id}"
