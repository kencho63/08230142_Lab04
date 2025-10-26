# ...existing code...
from django.shortcuts import render
from .models import LearningJourney, AboutMe

def index(request):
    journeys = LearningJourney.objects.all().order_by('-date_started')
   
    return render(request, 'kzjourney/index.html', {'journeys': journeys})

def aboutMe(request):
    abouts = AboutMe.objects.all()
    return render(request, 'kzjourney/aboutMe.html', {'abouts': abouts})
# ...existing code...
