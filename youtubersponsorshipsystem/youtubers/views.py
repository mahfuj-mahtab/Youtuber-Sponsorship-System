from django.shortcuts import render
from .models import Youtubers
# Create your views here.
def youtubers(request):
    tubers = Youtubers.objects.order_by('-created_date')
    data = {
        'tubers': tubers
    }
    return render(request, 'webpages/youtubers.html', data)
def youtubers_details(request, id):
    tuber = Youtubers.objects.filter(id = id)
    print(tuber)
    data = {
        'tuber': tuber[0]
    }
    return render(request, 'webpages/youtuber_detail.html', data)
def searchfunc(request):
    if request.method == 'GET':
        keyword = request.GET['keyword']
        youtuber = Youtubers.objects.filter(description__contains = keyword)
        data = {
            "youtuber" : youtuber
        }
        return render(request,'webpages/search.html',data) 
