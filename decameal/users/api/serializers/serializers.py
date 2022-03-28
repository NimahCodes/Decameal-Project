from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "username",
            "url",
            "id",
            "first_name",
            "last_name",
            "is_staff",
            "is_active",
            "date_joined",
            "is_verified",
            "email",
            "role",
            "otp",
            "mobile_number",
        ]

        extra_kwargs = {"url": {"view_name": "api:user-detail", "lookup_field": "id"}}
