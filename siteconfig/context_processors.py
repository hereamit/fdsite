from .models import SiteSettings

def site_settings(request):
    settings_obj = SiteSettings.objects.first()
    return {"site": settings_obj}
