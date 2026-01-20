from django.db import models

# Create your models here.

class SiteSettings(models.Model):
    company_name = models.CharField(max_length=120, default="Fine Diamond Education Foundation Pvt. Ltd.")
    tagline = models.CharField(max_length=160, blank=True, default="Pvt. Ltd. • Kathmandu, Nepal")

    logo = models.ImageField(upload_to="branding/", blank=True, null=True)

    phone = models.CharField(max_length=40, blank=True, default="+977-1-5911111")
    email = models.EmailField(blank=True, default="info@finediamond.edu.np")
    address = models.CharField(max_length=200, blank=True, default="Dharma Chakra Galli, Badhbazar, Kathmandu, Nepal")

    # Optional social links
    facebook = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    youtube = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)

    # Optional Google map embed url
    google_map_embed = models.TextField(blank=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Site Settings"