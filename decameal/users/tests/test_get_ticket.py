from django.urls import resolve, reverse
from rest_framework.test import APITestCase


class TestGetTicket(APITestCase):
    def test_get_ticket_url(self):
        assert reverse("api:tickets") == "/api/v1/tickets/"

    def test_get_ticket_url_with_view_name(self):
        assert resolve("/api/v1/tickets/").view_name == "api:tickets"
