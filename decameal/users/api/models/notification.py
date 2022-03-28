import uuid

from django.contrib.auth import get_user_model
from django.db import models

from .kitchen_staff import KitchenStaffProfile

User = get_user_model()


class Notification(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    kitchen_staff_id = models.ForeignKey(KitchenStaffProfile, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id}"
