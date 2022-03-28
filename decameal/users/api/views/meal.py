from decouple import config
from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response

from decameal.users.api.models.meal import Meal
from decameal.utils.cloudinary_interface import CloudinaryInterface

from ..permissions.meal import IsKitchenStaffOrReadOnly
from ..serializers.meal import MealSerializer, MealUploadSerializer


class Meals(ListCreateAPIView):
    permission_classes = [IsKitchenStaffOrReadOnly]
    serializer_class = MealSerializer
    queryset = Meal.objects.all()

    def create(self, request):
        cover_img = request.data.get("cover_img", "")

        data = request.data
        serializer = MealUploadSerializer(data=data)
        if not serializer.is_valid():
            return Response(
                {
                    "message": "failure",
                    "data": "null",
                    "errors": serializer.errors,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        cover_img_url = CloudinaryInterface.upload_image(
            cover_img, folder_name=config("CLOUD_MEAL_FOLDER")
        )

        if not cover_img_url:
            return Response(
                {
                    "message": "failure",
                    "data": "null",
                    "errors": {
                        "cover_img": "Image upload failed, please make sure you are uploading a valid image format"
                    },
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        get_cover_img_url = cover_img_url.get("url")

        serializer.save(cover_img=get_cover_img_url)
        serializer_dict = dict(serializer.data)
        serializer_dict["cover_img"] = get_cover_img_url

        return Response(
            {
                "message": "success",
                "data": {"meals": serializer_dict},
                "error": "null",
            },
            status=status.HTTP_201_CREATED,
        )

    def list(self, request):
        queryset = Meal.objects.all().order_by("-created_at")
        serializer_class = MealSerializer(data=queryset, many=True)
        serializer_class.is_valid()
        return Response(
            {
                "message": "success",
                "data": {
                    "meals": serializer_class.data,
                    "total": self.queryset.count(),
                },
                "error": "null",
            },
            status=status.HTTP_200_OK,
        )
