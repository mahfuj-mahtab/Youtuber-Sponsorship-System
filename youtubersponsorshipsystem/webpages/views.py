from django.shortcuts import render,HttpResponse
from .models import Slider,Team
from youtubers.models import Youtubers
# Create your views here.
def home(request):
    slider = Slider.objects.all()
    teams = Team.objects.all()
    youtubers = Youtubers.objects.all().order_by('-created_date').filter(is_featured = True)
    data = {
        'slides' : slider,
        'teams' : teams,
        'featureyoutubers' : youtubers, 
    }

    return render(request,"webpages/home.html",data)
def about(request):
    return render(request,"webpages/about.html")
def service(request):
    return HttpResponse ('hello')
def contact(request):
    return HttpResponse ('hello')
    
    