"""
Admin config for users app.
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin

from .models import User


@admin.register(User)
class CustomUserAdmin(AuthUserAdmin):
    """Admin class for custom user."""

    list_display = ("username", "is_superuser")
    search_fields = ["username"]
