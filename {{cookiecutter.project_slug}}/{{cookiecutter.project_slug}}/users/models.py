"""
Models for Users app.
"""
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Customized user model class."""

    def __str__(self):
        return self.username
