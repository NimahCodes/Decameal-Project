from rest_framework import serializers

from ...models import User


class OTPVerifySerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    otp = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ["otp", "email"]
