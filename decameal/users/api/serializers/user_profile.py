from rest_framework import serializers

from ..models.decadev import DecadevProfile
from ..models.kitchen_staff import KitchenStaffProfile
from ..models.staff import StaffProfile


class DecadevProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = DecadevProfile
        fields = [
            "avatar",
            "stack",
            "address",
            "gender",
        ]


class StaffProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffProfile
        fields = [
            "avatar",
            "bio",
            "address",
            "gender",
        ]


class KitchenStaffProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = KitchenStaffProfile
        fields = [
            "avatar",
            "bio",
            "address",
            "gender",
        ]
