"""
Admin config for core app.
"""
from django.conf import settings
from django.contrib import admin
from django.contrib.sites.models import Site

# Unregister extra apps
admin.site.unregister(Site)

# Admin site configuration
admin.site.site_header = settings.ADMIN_SITE_HEADER
admin.site.site_title = settings.ADMIN_SITE_HEADER
