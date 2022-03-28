import pytest
from django.urls import reverse
from rest_framework.test import APIClient, APITestCase

from decameal.users.api.models.meal import Meal
from decameal.users.api.models.meal_category import MealCategory
from decameal.users.api.models.ticket import Ticket
from decameal.users.api.models.ticket_tracker import TicketTracker
from decameal.users.models import User

pytestmark = pytest.mark.django_db
LOGIN_URL = reverse("api:login")
REGISTER_URL = reverse("api:register")


class TestSetup(APITestCase):
    def test_update_without_permission(self):
        payload = {
            "id": 1,
            "email": "test@decagon.dev",
            "username": "tester",
            "first_name": "test",
            "last_name": "testingangle",
            "mobile_number": "080419419",
            "password": "testingun",
            "role": "Kitchen Staff",
        }

        client = APIClient()
        client.post(REGISTER_URL, payload)
        user = User.objects.get(email="test@decagon.dev")
        user.is_verified = True
        user.save()

        meal_category = MealCategory.objects.create(
            id="88dc9faf-609f-4e53-87db-5488de4b526a", name="swallow"
        )
        meal_category.save()

        meal = Meal.objects.create(
            id="88dc9faf-609f-4e53-87db-5488de4b526a",
            title="EGUSI",
            description="Fresh egusi and beef",
            category_id=meal_category,
        )
        meal.save()

        ticket = Ticket.objects.create(
            id="88dc9faf-609f-4e53-87db-5488de4b526a",
            ticket_no="00016",
            lunch=meal,
            dinner=meal,
            scheduled_date="2022-02-21",
        )
        ticket.save()

        ticket_tracker = TicketTracker.objects.create(
            id="88dc9faf-609f-4e53-87db-5488de4b526a",
            user_id=user,
            ticket_id=ticket,
        )
        ticket_tracker.save()
        update = client.put(
            "/api/v1/tickettraker/\
            88dc9faf-609f-4e53-87db-5488de4b526a/\
                subscriber/1/88dc9faf-609f-4e53-87db-5488de4b526a/\
                    dinner/",
            dinner=True,
        )
        assert update.status_code == 404
