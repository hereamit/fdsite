from django.contrib import admin

from .models import HomeSection, HomeCard

# Register your models here.

from .models import Slide

@admin.register(Slide)

class SlideAdmin(admin.ModelAdmin):
  list_display = ("destination", "title", "order", "is_active")
  list_editable = ("order", "is_active")
  search_fields = ("destination", "title")
  


class HomeCardInline(admin.TabularInline):
    model = HomeCard
    extra = 0
    fields = ("order", "is_active", "icon", "title", "description", "action_type", "url_name", "modal_id")
    ordering = ("order",)

@admin.register(HomeSection)
class HomeSectionAdmin(admin.ModelAdmin):
    list_display = ("title", "is_active")
    inlines = [HomeCardInline]
