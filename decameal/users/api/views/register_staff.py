import os

from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from decameal.users.api.models.staff import StaffProfile
from decameal.users.models import User
from decameal.utils.helper import Helper

from ..serializers.register_serializer import RegisterSerializer


class RegisterStaffView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    def post(self, request):
        data = request.data
        email = data.get("email", "")
        serializer = self.serializer_class(data=data)

        if not serializer.is_valid():
            return Response(
                {"message": "failure", "data": "null", "errors": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )

        otp = Helper.generate_OTP(6)
        user = serializer.validated_data

        BASE_URL = os.environ.get("BASE_URL", "http://localhost:8000/api/")
        EMAIL_VERIFICATION_URL = BASE_URL + f"auth/verify/?otp={otp}&email={email}"
        email_body = (
            "Hi "
            + user["username"]
            + " Use the link below to verify your email \n"
            + EMAIL_VERIFICATION_URL
        )
        data = {
            "email_body": email_body,
            "to_email": user["email"],
            "email_subject": "Please Verify Your Email",
        }
        Helper.send_mail(data)

        serializer.save()
        user = User.objects.get(username=user["username"])
        user.otp = otp
        user.role = "Staff"
        user.save()

        staff = StaffProfile.objects.create(user_id=user)
        staff.save()

        data = dict()
        data = serializer.data
        data["otp"] = otp
        data["role"] = user.role

        return Response(
            {"message": "success", "data": data, "errors": "null"},
            status=status.HTTP_200_OK,
        )
