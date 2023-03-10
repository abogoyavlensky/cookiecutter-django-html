"""
Seetings for Users app.
"""
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    """Config for users app."""

    name = "{{cookiecutter.project_slug}}.users"
    verbose_name = _("Users")
