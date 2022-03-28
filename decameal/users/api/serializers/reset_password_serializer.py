from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class SetNewPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(
        min_length=6, max_length=68, write_only=True, required=True
    )
    confirm_password = serializers.CharField(
        min_length=6, max_length=68, write_only=True, required=True
    )

    class Meta:
        fields = ["email", "password", "confirm password"]
