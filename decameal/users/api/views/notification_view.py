from rest_framework import generics, status
from rest_framework.response import Response

from ...models import User
from ..models.kitchen_staff import KitchenStaffProfile
from ..models.notification import Notification
from ..permissions.notification import Notifications
from ..serializers.notification_serializer import (
    GetNotificationSerializer,
    SendNotificationSerializer,
)


class NotificationView(generics.GenericAPIView):
    permission_classes = [Notifications]

    def post(self, request, pk):
        user = User.objects.get(pk=pk)
        kitchen_staff_id = KitchenStaffProfile.objects.get(user_id=request.user.id)
        message = request.data.get("message", "")
        serializer = SendNotificationSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                {"message": "failure", "data": "null", "error": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )
        notification = Notification.objects.create(
            user_id=user, kitchen_staff_id=kitchen_staff_id, message=message
        )
        notification.save()
        sent_notification = GetNotificationSerializer(notification)

        return Response(
            {"message": "success", "data": sent_notification.data, "error": "null"},
            status=status.HTTP_200_OK,
        )

    def get(self, request, pk):
        user = User.objects.get(pk=pk)
        notifications = Notification.objects.filter(user_id=user).order_by(
            "-updated_at"
        )
        serializer = GetNotificationSerializer(notifications, many=True)
        return Response(
            {
                "message": "success",
                "data": {
                    "notifications": serializer.data,
                    "total": len(serializer.data),
                },
                "errors": "null",
            },
            status=status.HTTP_200_OK,
        )
