"""
Common configuration for tests.
"""
import pytest
from django.contrib.auth import get_user_model
from django_dynamic_fixture import G

@pytest.fixture
def user():
    user = G(get_user_model(), username='user')
    user.set_password('user')
    user.save()
    return user
