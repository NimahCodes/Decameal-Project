from django.urls import reverse
from faker import Faker
from rest_framework.test import APITestCase


class TestSetup(APITestCase):
    def setUp(self):
        self.register_url = reverse("api:register")
        self.faker = Faker()
        self.user_data = {
            "email": self.faker.email(),
            "username": self.faker.email().split("@")[0],
            "password": self.faker.email(),
        }
        return super().setUp()

    def tearDown(self):
        return super().tearDown()
