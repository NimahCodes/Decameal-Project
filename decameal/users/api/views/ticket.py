from rest_framework import status, views
from rest_framework.response import Response

from decameal.users.api.models.meal import Meal
from decameal.users.api.models.ticket import Ticket

from ..permissions.meal import IsKitchenStaffOrReadOnly
from ..serializers.meal import MealSerializer
from ..serializers.meal_ticket_serializer import MealTicketSerializer
from ..views.utils import TicketNum


class TicketView(views.APIView):
    serializer_class = MealTicketSerializer
    permission_classes = [IsKitchenStaffOrReadOnly]

    def get(self, request):
        tickets = Ticket.objects.all()
        serializer = self.serializer_class(tickets, many=True)
        for data in serializer.data:
            lunch = Meal.objects.get(id=data["lunch"])
            dinner = Meal.objects.get(id=data["dinner"])
            lunch_serializer = MealSerializer(lunch)
            dinner_serializer = MealSerializer(dinner)
            data["lunch"] = lunch_serializer.data
            data["dinner"] = dinner_serializer.data

        return Response(
            {
                "message": "success",
                "data": {"tickets": serializer.data, "total": len(tickets)},
                "error": "null",
            },
            status=status.HTTP_200_OK,
        )

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            return Response(
                {"message": "failure", "data": "null", "error": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )

        ticket_no_list = Ticket.objects.values_list("ticket_no", flat=True)
        ticket_no = TicketNum.create_ticket_number(3)
        while ticket_no in ticket_no_list:
            ticket_no = TicketNum.create_ticket_number(3)
        serializer.validated_data["ticket_no"] = ticket_no
        serializer.save()
        serializer_dict = dict(serializer.data)
        return Response(
            {
                "message": "success",
                "data": {"ticket": serializer_dict},
                "error": "null",
            },
            status=status.HTTP_201_CREATED,
        )
