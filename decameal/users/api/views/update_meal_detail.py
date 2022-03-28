from django.core.exceptions import ObjectDoesNotExist
from rest_framework import generics, status
from rest_framework.response import Response

from decameal.users.api.models.meal import Meal

from ..permissions.update_meal_detail import IsKitchenStaff
from ..serializers.update_meal_detail_serializer import UpdateMealDetailSerializer


class UpdateMealDetailView(generics.UpdateAPIView):

    queryset = Meal.objects.all()
    permission_classes = (IsKitchenStaff,)
    serializer_class = UpdateMealDetailSerializer

    def put(self, request, pk):
        try:
            meal = Meal.objects.get(id=pk)
        except ObjectDoesNotExist:
            return Response(
                {
                    "message": "failure",
                    "data": "null",
                    "error": {"Meal": "Meal does not exist"},
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        serializer = self.serializer_class(meal, data=request.data)
        if not serializer.is_valid():
            return Response(
                {"message": "failure", "data": "null", "error": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )
        if serializer.is_valid():

            serializer.save()

        serializer_dict = dict(serializer.data)
        return Response(
            {
                "message": "success",
                "data": {
                    "meals": serializer_dict,
                },
                "error": "null",
            },
            status=status.HTTP_200_OK,
        )
