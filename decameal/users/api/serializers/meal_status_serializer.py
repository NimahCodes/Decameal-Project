from rest_framework import serializers

from ..models.ticket_tracker import TicketTracker


class TicketTrackerSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketTracker
        fields = "__all__"
