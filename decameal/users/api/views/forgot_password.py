import os

from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status, views
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from ..serializers.forgot_password_serializer import ForgetPasswordSerializer
from .utils import Util

User = get_user_model()


class ForgetPasswordView(views.APIView):
    serializer_class = ForgetPasswordSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        data = request.data
        email = request.data.get("email", "")
        serializer = self.serializer_class(data=data)
        if not serializer.is_valid():
            return Response(
                {"message": "failure", "data": "null", "errors": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )
        try:
            user = User.objects.filter(email=email)
        except ObjectDoesNotExist:
            return Response(
                {
                    "message": "failure",
                    "data": "null",
                    "errors": {"email": "This email does not exist"},
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        if not user:
            return Response(
                {
                    "message": "failure",
                    "data": "null",
                    "errors": {"email": "This email does not exist"},
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        if not user.first().is_verified:
            return Response(
                {
                    "message": "failure",
                    "data": "null",
                    "errors": {"email": "This email is not verified"},
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        BASE_URL = os.environ.get("BASE_URL", "http://localhost:8000/api/")
        absurl = BASE_URL + "auth/reset-password"
        email_body = f"""Hi,{user.first().username}
            Use this link to reset your password {absurl}  """

        data = {
            "to_email": user.first().email,
            "email_subject": "Please Reset Your Passsword",
            "email_body": email_body,
        }
        Util.send_email(data)
        report = Util.send_email(data)
        print(report)
        return Response(
            {
                "message": "success",
                "data": {"email": "Email has been sent"},
                "errors": "null",
            },
            status=status.HTTP_200_OK,
        )
