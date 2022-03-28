from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        style={"input_type": "email", "placeholder": "Email"},
    )

    class Meta:
        model = User
        fields = ["email", "password"]
        extra_kwargs = {
            "password": {
                "required": True,
                "style": {"input_type": "password", "placeholder": "Password"},
            },
        }
