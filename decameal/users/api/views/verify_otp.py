from django.core.exceptions import ObjectDoesNotExist
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from ...models import User
from ..serializers.otp_verify_serializer import OTPVerifySerializer


class OTPVerifyView(generics.GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = OTPVerifySerializer

    def post(self, request):
        data = request.data
        otp = data.get("otp", "")
        email = data.get("email", "")
        serializer = self.serializer_class(data=data)
        if not serializer.is_valid():
            return Response(
                {"message": "failure", "data": "null", "errors": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )
        try:
            user = User.objects.get(email=email)
        except ObjectDoesNotExist:
            return Response(
                {
                    "message": "failure",
                    "data": "null",
                    "errors": {"email": "This email does not exist"},
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        if user.otp != otp:
            return Response(
                {
                    "message": "failure",
                    "data": "null",
                    "error": "Please provide a valid otp code",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        user.is_verified = True
        user.save()
        return Response(
            {
                "message": "success",
                "data": "Congrats, your account have been successfully verified",
                "error": "null",
            },
            status=status.HTTP_200_OK,
        )
