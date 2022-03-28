from rest_framework import serializers

from ..models.notification import Notification


class GetNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = "__all__"


class SendNotificationSerializer(serializers.ModelSerializer):
    # message = serializers.TextField(required=True)
    message = serializers.CharField(required=True, max_length=300)

    class Meta:
        model = Notification
        fields = "__all__"
        read_only_fields = [
            "id",
            "user_id",
            "kitchen_staff_id",
            "created_at",
            "updated_at",
        ]
