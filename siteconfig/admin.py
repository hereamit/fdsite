from django.contrib import admin

# Register your models here.

from .models import SiteSettings

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    pass
