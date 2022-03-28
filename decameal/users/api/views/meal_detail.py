from django.core.exceptions import ObjectDoesNotExist
from rest_framework import generics, status
from rest_framework.response import Response

from decameal.users.api.models.meal import Meal

from ..permissions.meal import IsKitchenStaffOrReadOnly
from ..serializers.meal import MealSerializer
from ..serializers.update_meal_detail_serializer import UpdateMealDetailSerializer


class MealDetail(generics.GenericAPIView):
    serializer_class = MealSerializer
    permission_classes = (IsKitchenStaffOrReadOnly,)

    def get(self, request, pk):
        try:
            meal = Meal.objects.get(id=pk)
        except ObjectDoesNotExist:
            return Response(
                {
                    "message": "failure",
                    "data": "null",
                    "error": {"meal": "Meal does not exist"},
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        serializer_class = MealSerializer(meal)
        return Response(
            {
                "message": "success",
                "data": {
                    "meal": serializer_class.data,
                },
                "error": "null",
            },
            status=status.HTTP_200_OK,
        )

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
        serializer = UpdateMealDetailSerializer(meal, data=request.data)
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

    def delete(self, request, pk):
        try:
            meal = Meal.objects.get(id=pk)
            meal.delete()
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
                    "error": {"meal": "Meal does not exist"},
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
