from rest_framework import serializers

from ..models.ticket import Ticket


class MealTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = "__all__"
        read_only_fields = ("id", "ticket_no", "created_at", "updated_at")


class UpdateMealTicketsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ("id", "lunch", "dinner")
        read_only_fields = (
            "id",
            "ticket_no",
            "scheduled_date" "created_at",
            "updated_at",
        )
