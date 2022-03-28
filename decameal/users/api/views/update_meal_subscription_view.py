from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ...models import User
from ..models.decadev import DecadevProfile
from ..models.staff import StaffProfile
from ..permissions.update_meal_subscription import IsDecadevOrStaff


def get_profile(user):
    profile = (
        DecadevProfile.objects.get(user_id=user)
        if user.role == "Decadev"
        else StaffProfile.objects.get(user_id=user)
    )
    return profile


def update_meal_subscription_status(profile):
    profile.is_subscribed = not profile.is_subscribed
    profile.save()


class UpdateMealSubscriptionView(APIView):
    permission_classes = [
        IsDecadevOrStaff,
    ]

    def put(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response(
                {
                    "message": "failure",
                    "data": "null",
                    "error": {"user": "User does not exist"},
                },
                status=status.HTTP_404_NOT_FOUND,
            )
        user_profile = get_profile(user)
        update_meal_subscription_status(user_profile)
        return Response(
            {
                "message": "success",
                "data": {
                    "user_id": user_id,
                    "is_subscribed": user_profile.is_subscribed,
                },
                "error": "null",
            },
            status=status.HTTP_200_OK,
        )
