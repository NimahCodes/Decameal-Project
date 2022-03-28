from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status, views
from rest_framework.response import Response

from ..models.ticket import Ticket
from ..permissions.ticket import IsKitchenStaff
from ..serializers.meal_ticket_serializer import UpdateMealTicketsSerializer


class UpdateTicketView(views.APIView):
    serializer_class = UpdateMealTicketsSerializer
    permission_classes = (IsKitchenStaff,)

    def put(self, request, pk):
        try:
            ticket = Ticket.objects.get(id=pk)
        except ObjectDoesNotExist:
            return Response(
                {
                    "message": "failure",
                    "data": "null",
                    "error": {"ticket": "Ticket does not exist"},
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        serializer = self.serializer_class(ticket, data=request.data)
        if not serializer.is_valid():
            return Response(
                {"message": "failure", "data": "null", "error": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )
        if serializer.is_valid():
            lunch = serializer.validated_data["lunch"]
            dinner = serializer.validated_data["dinner"]
            ticket.lunch = lunch
            ticket.dinner = dinner
            serializer.save()

        serializer_dict = dict(serializer.data)
        serializer_dict["scheduled_date"] = ticket.scheduled_date.strftime("%Y-%m-%d")
        serializer_dict["created_at"] = ticket.created_at.strftime("%Y-%m-%d %H:%M:%S")
        serializer_dict["updated_at"] = ticket.updated_at.strftime("%Y-%m-%d %H:%M:%S")
        return Response(
            {
                "message": "success",
                "data": {"ticket": serializer_dict},
                "error": "null",
            },
            status=status.HTTP_201_CREATED,
        )

    def delete(self, request, pk):
        try:
            ticket = Ticket.objects.get(id=pk)
            ticket.delete()
            return Response(
                {
                    "message": "success",
                    "data": {},
                    "error": "null",
                },
                status=status.HTTP_204_NO_CONTENT,
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
