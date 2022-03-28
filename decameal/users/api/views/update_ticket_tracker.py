from django.core.exceptions import ObjectDoesNotExist
from rest_framework import generics, status
from rest_framework.response import Response

from decameal.users.api.models.ticket_tracker import TicketTracker

from ..permissions.update_ticket_tracker import IsKitchenStaff
from ..serializers.meal_status_serializer import TicketTrackerSerializer


class UpdateTicketTrackerLunchView(generics.UpdateAPIView):
    queryset = TicketTracker.objects.all()
    permission_classes = (IsKitchenStaff,)
    serializer_class = TicketTrackerSerializer

    def put(self, request, pk, user_id):
        try:
            ticket_tracker = TicketTracker.objects.get(ticket_id=pk, user_id=user_id)
        except ObjectDoesNotExist:
            return Response(
                {
                    "message": "failure",
                    "data": "null",
                    "error": {
                        "ticket_status": "No such instance exist for user or ticket"
                    },
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        # Invert status of lunch collected
        ticket_tracker.lunch_collected = not ticket_tracker.lunch_collected
        ticket_tracker.save()

        serializer = self.serializer_class(ticket_tracker)
        return Response(
            {
                "message": "success",
                "data": serializer.data,
                "error": "null",
            },
            status=status.HTTP_200_OK,
        )


class UpdateTicketTrackerDinnerView(generics.UpdateAPIView):
    queryset = TicketTracker.objects.all()
    permission_classes = (IsKitchenStaff,)
    serializer_class = TicketTrackerSerializer

    def put(self, request, pk, user_id):
        try:
            ticket_tracker = TicketTracker.objects.get(ticket_id=pk, user_id=user_id)
        except ObjectDoesNotExist:
            return Response(
                {
                    "message": "failure",
                    "data": "null",
                    "error": {
                        "ticket_status": "No such instance exist for user or ticket"
                    },
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        # Invert status of dinner collected
        ticket_tracker.dinner_collected = not ticket_tracker.dinner_collected
        ticket_tracker.save()

        serializer = self.serializer_class(ticket_tracker)
        return Response(
            {
                "message": "success",
                "data": serializer.data,
                "error": "null",
            },
            status=status.HTTP_200_OK,
        )
