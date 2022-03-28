from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class User(AbstractUser):
    """
    Default custom user model for Decameal.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    ROLES_CHOICES = (
        ("Decadev", "Decadev"),
        ("Staff", "Staff"),
        ("Kitchen Staff", "Kitchen Staff"),
    )
    #: First and last name do not cover name patterns around the globe
    is_verified = models.BooleanField(default=False)
    email = models.EmailField(unique=True)
    mobile_number = models.CharField(max_length=255, null=True)
    otp = models.CharField(max_length=200, null=True)
    role = models.CharField(
        max_length=255, default="Decadev", null=True, choices=ROLES_CHOICES
    )

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})
