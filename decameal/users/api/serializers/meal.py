from rest_framework import serializers

from decameal.users.api.models.meal import Meal


class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ["id", "title", "description", "cover_img", "category_id"]


class MealUploadSerializer(serializers.ModelSerializer):
    cover_img = serializers.FileField(required=True)

    class Meta:
        model = Meal
        fields = ["id", "title", "description", "cover_img", "category_id"]
