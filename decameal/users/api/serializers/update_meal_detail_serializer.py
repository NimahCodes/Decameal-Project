from rest_framework import serializers

from decameal.users.api.models.meal import Meal


class UpdateMealDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ["title", "description", "cover_img", "category_id"]
        extra_kwargs = {
            "title": {"required": False},
            "description": {"required": False},
            "cover_img": {"required": False},
            "category_id": {"required": False},
        }
