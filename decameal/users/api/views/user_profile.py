from rest_framework import generics, permissions, status
from rest_framework.response import Response

from ...models import User
from ..models.decadev import DecadevProfile
from ..models.kitchen_staff import KitchenStaffProfile
from ..models.staff import StaffProfile
from ..serializers.user_profile import (
    DecadevProfileSerializer,
    KitchenStaffProfileSerializer,
    StaffProfileSerializer,
)
from ..serializers.user_serializer import UserSerializer


def get_profile(user):
    if user.role == "Decadev":
        profile = DecadevProfile.objects.get(user_id=user)
        serializer = DecadevProfileSerializer(profile)
    elif user.role == "Staff":
        profile = StaffProfile.objects.get(user_id=user)
        serializer = StaffProfileSerializer(profile)
    else:
        profile = KitchenStaffProfile.objects.get(user_id=user)
        serializer = KitchenStaffProfileSerializer(profile)
    return serializer


class UserProfileView(generics.GenericAPIView):
    permission_classes = [
        permissions.AllowAny,
    ]

    def get(self, request, pk):
        try:
            user = User.objects.get(id=pk)
            user_data = UserSerializer(user)
        except User.DoesNotExist:
            return Response(
                {
                    "message": "failure",
                    "data": "null",
                    "error": {"user": "User does not exist"},
                },
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = get_profile(user)
        serializer_dict = dict(serializer.data)
        serializer_dict["user"] = user_data.data
        return Response(
            {
                "message": "success",
                "data": serializer_dict,
                "error": "null",
            },
            status=status.HTTP_200_OK,
        )
