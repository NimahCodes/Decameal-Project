# from django.contrib.auth import get_user_model
from rest_framework import serializers

from ...models import User
from ..models.ticket import Ticket
from ..models.ticket_tracker import TicketTracker


class TicketGenerateSerializer(serializers.ModelSerializer):

    ticket_id = serializers.PrimaryKeyRelatedField(queryset=Ticket.objects.all())
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.filter(role__in=["Decadev", "Staff"])
    )

    class Meta:
        model = TicketTracker
        fields = ["ticket_id", "user_id"]
