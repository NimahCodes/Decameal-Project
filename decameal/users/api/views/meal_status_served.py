from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models.ticket_tracker import Ticket, TicketTracker
from ..permissions.ticket import IsKitchenStaff
from ..serializers.meal_status_serializer import TicketTrackerSerializer


class MealStatus(APIView):
    serializer_class = TicketTrackerSerializer
    permission_classes = (IsKitchenStaff,)

    def get(self, request, pk):
        try:
            ticket = Ticket.objects.get(id=pk)
            meal_status = TicketTracker.objects.filter(ticket_id=ticket.id)
            serializer = self.serializer_class(meal_status, many=True)
            return Response(
                {
                    "message": "success",
                    "data": {"tickets": serializer.data, "total": len(meal_status)},
                    "error": "null",
                },
                status=status.HTTP_200_OK,
            )
        except ObjectDoesNotExist:
            return Response(
                {
                    "message": "failure",
                    "data": "null",
                    "error": {"ticket": "Ticket does not exist"},
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
