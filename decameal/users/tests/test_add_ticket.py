import pytest
from django.urls import resolve, reverse
from rest_framework.test import APIClient, APITestCase

pytestmark = pytest.mark.django_db
register_url = reverse("api:tickets")


class TestUser(APITestCase):
    def setUp(self):

        self.client = APIClient()

    def test_add_ticket_url(self):
        assert reverse("api:tickets") == "/api/v1/tickets/"
        assert resolve("/api/v1/tickets/").view_name == "api:tickets"
