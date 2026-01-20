from django.db import models

# Create your models here.


class Slide(models.Model):
    destination = models.CharField(max_length=50)  # Japan/UK/Australia
    kicker = models.CharField(max_length=120, blank=True)  # emoji + text
    title = models.CharField(max_length=160)
    description = models.TextField(blank=True)

    # Background image uploaded from admin
    bg_image = models.ImageField(upload_to="slides/")

    # Buttons (so you can change text & link from admin)
    primary_text = models.CharField(max_length=60, default="Explore Services")
    primary_url_name = models.CharField(max_length=60, default="services")  # Django url name

    secondary_text = models.CharField(max_length=60, default="Free Counseling")
    secondary_type = models.CharField(
        max_length=10,
        choices=[("url", "URL"), ("modal", "Modal")],
        default="modal"
    )
    secondary_url_name = models.CharField(max_length=60, blank=True)  # used if secondary_type = url

    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.destination} - {self.title}"



class HomeSection(models.Model):
    # This controls the heading text of the section
    title = models.CharField(max_length=120, default="Everything You Need — In One Place")
    subtitle = models.CharField(max_length=200, blank=True, default="Quick overview of our pages. Click any section to explore more.")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Home Section ({'Active' if self.is_active else 'Inactive'})"


class HomeCard(models.Model):
    # This controls each card
    section = models.ForeignKey(HomeSection, on_delete=models.CASCADE, related_name="cards")

    icon = models.CharField(max_length=10, default="✨")  # emoji like 🏢 🧭 📸
    title = models.CharField(max_length=80)
    description = models.CharField(max_length=220)

    # Link behavior: either go to a URL name or open modal
    action_type = models.CharField(
        max_length=10,
        choices=[("url", "URL"), ("modal", "Modal")],
        default="url"
    )
    url_name = models.CharField(max_length=60, blank=True)     # e.g. about, services, gallery
    modal_id = models.CharField(max_length=60, blank=True)     # e.g. counselModal (if you use modal)

    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.title
