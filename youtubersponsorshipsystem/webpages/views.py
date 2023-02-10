from django.shortcuts import render,HttpResponse
from .models import Slider,Team
# Create your views here.
def home(request):
    slider = Slider.objects.all()
    teams = Team.objects.all()
    data = {
        'slides' : slider,
        'teams' : teams
    }

    return render(request,"webpages/home.html",data)
def about(request):
    return render(request,"webpages/about.html")
def service(request):
    return HttpResponse ('hello')
def contact(request):
    return HttpResponse ('hello')
    
    