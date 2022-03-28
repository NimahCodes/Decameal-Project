import pytest
from django.urls import reverse
from rest_framework.test import APITestCase

pytestmark = pytest.mark.django_db

swagger_docs_url = reverse("schema-swagger-ui")


class TestSwaggerUI(APITestCase):
    def test_swagger_ui_url(self):
        assert swagger_docs_url == "/api/api.json/"
