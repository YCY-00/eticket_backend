from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, DateField, BooleanField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """
    Default custom user model for backend.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    # First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = CharField(_("First Name of User"), blank=True, max_length=255)  # type: ignore
    last_name = CharField(_("Last Name of User"), blank=True, max_length=255)  # type: ignore

    birthdate = DateField(null=True, blank=True)
    phone_number = CharField(max_length=20, null=True, blank=True)
    gender = CharField(max_length=1, null=True, blank=True)
    is_admin = BooleanField(default=False)
    is_organizer = BooleanField(default=False)

    def get_absolute_url(self) -> str:
        """Get URL for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})
