from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return render(request,"webpages/home.html")
def about(request):
    return render(request,"webpages/about.html")
def service(request):
    return HttpResponse ('hello')
def contact(request):
    return HttpResponse ('hello')
    
    