from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from ..serializers.reset_password_serializer import SetNewPasswordSerializer

User = get_user_model()


class SetNewPasswordView(generics.GenericAPIView):
    serializer_class = SetNewPasswordSerializer
    permission_classes = (AllowAny,)

    def put(self, request):
        data = request.data
        email = data.get("email", "")
        password = data.get("password", "")
        confirm_password = data.get("confirm_password", "")
        serializer = self.serializer_class(data=request.data)
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
        if password != confirm_password:
            return Response(
                {
                    "message": "failure",
                    "data": "null",
                    "errors": {"password": "Passwords do not match"},
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        user.set_password(password)
        user.save()
        return Response(
            {
                "message": "success",
                "data": "Congrats, your password has been successfully changed",
                "error": "null",
            },
            status=status.HTTP_200_OK,
        )
