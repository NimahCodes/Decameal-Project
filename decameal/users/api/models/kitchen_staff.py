import uuid

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class KitchenStaffProfile(models.Model):
    GENDER_CHOICES = (
        ("Male", "Male"),
        ("Female", "Female"),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    avatar = models.URLField(null=True)
    address = models.CharField(max_length=255, null=True)
    bio = models.CharField(max_length=255, null=True)
    gender = models.CharField(max_length=255, null=True, choices=GENDER_CHOICES)

    def __str__(self):
        return f"{self.user_id}"
