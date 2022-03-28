from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from ...models import User


class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(max_length=68, min_length=6, write_only=True)
    email = serializers.EmailField(
        required=True, validators=[UniqueValidator(queryset=User.objects.all())]
    )

    class Meta:
        model = User
        fields = [
            "email",
            "password",
            "username",
        ]

    def validate(self, attrs):
        email = attrs.get("email", "")
        if email == "":
            raise serializers.ValidationError("Email is required")
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({"email": "Email already exists"})
        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
