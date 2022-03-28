import uuid

from django.db import models

from .meal import Meal


class Ticket(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ticket_no = models.CharField(max_length=255, null=False, unique=True)
    lunch = models.ForeignKey(Meal, on_delete=models.CASCADE, related_name="lunch")
    dinner = models.ForeignKey(Meal, on_delete=models.CASCADE, related_name="dinner")
    scheduled_date = models.DateField(blank=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id}"
