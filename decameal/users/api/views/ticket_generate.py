from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models.ticket_tracker import TicketTracker
from ..permissions.ticket import IsKitchenStaff
from ..serializers.meal_status_serializer import TicketTrackerSerializer
from ..serializers.ticket_generate_serializer import TicketGenerateSerializer

User = get_user_model()


class GenerateTicketStatus(APIView):
    serializer_class = TicketGenerateSerializer
    permission_classes = [
        IsKitchenStaff,
    ]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            ticket_id = serializer.validated_data["ticket_id"]
            user_id = serializer.validated_data["user_id"]

            try:
                check_existing_ticket_status = TicketTracker.objects.filter(
                    ticket_id=ticket_id, user_id=user_id
                ).exists()
                if check_existing_ticket_status:
                    return Response(
                        {
                            "message": "failure",
                            "data": "null",
                            "error": {
                                "status": "Ticket status already generated for user"
                            },
                        },
                        status=status.HTTP_400_BAD_REQUEST,
                    )
            except ObjectDoesNotExist:
                print("Ticket does not exist")

            except Exception as error:
                return Response(
                    {"error": str(error)}, status=status.HTTP_400_BAD_REQUEST
                )

            ticket = TicketTracker.objects.create(
                ticket_id=ticket_id,
                user_id=user_id,
                lunch_collected=False,
                dinner_collected=False,
            )
            ticket.save()
            created_ticket = TicketTracker.objects.get(id=ticket.id)
            ticket_serializer = TicketTrackerSerializer(created_ticket)
            return Response(
                {
                    "message": "success",
                    "data": ticket_serializer.data,
                    "error": "null",
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(
            {"message": "failure", "data": "null", "error": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )
