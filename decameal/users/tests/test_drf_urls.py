import pytest
from django.urls import resolve, reverse

from decameal.users.models import User

pytestmark = pytest.mark.django_db


def test_user_detail(user: User):
    assert (
        reverse("api:user-detail", kwargs={"id": user.id})
        == f"/api/v1/users/{user.id}/"
    )
    assert resolve(f"/api/v1/users/{user.id}/").view_name == "api:user-detail"


def test_user_list():
    assert reverse("api:user-list") == "/api/v1/users/"
    assert resolve("/api/v1/users/").view_name == "api:user-list"


def test_user_me():
    assert reverse("api:user-me") == "/api/v1/users/me/"
    assert resolve("/api/v1/users/me/").view_name == "api:user-me"
