from django.shortcuts import render

from .models import Slide, HomeSection

# Create your views here.

def home(request):
  slides = Slide.objects.filter(is_active = True)
  return render(request, "home.html", {"slides": slides})

def about(request):
  return render(request, "about.html")

def services(request):
  return render(request, "services.html")

def gallery(request):
  return render(request, "gallery.html")

def blog(request):
  return render(request, "blog.html")

def contact(request):
  return render(request, "contact.html")

from .models import Slide, HomeSection

from .models import Slide, HomeSection, HomeCard

def home(request):
    slides = Slide.objects.filter(is_active=True)

    home_section = HomeSection.objects.filter(is_active=True).first()

    # Get all active cards from all active sections
    home_cards = HomeCard.objects.filter(
        is_active=True,
        section__is_active=True
    ).order_by("section__id", "order")

    return render(request, "home.html", {
        "slides": slides,
        "home_section": home_section,
        "home_cards": home_cards,
    })
