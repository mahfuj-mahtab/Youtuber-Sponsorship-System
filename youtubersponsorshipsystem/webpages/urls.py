from django.urls import path,include

from . import views
from webpages.views import *
urlpatterns = [
    path('',home,name = 'home'),
    path('about/',about,name = 'about'),
    path('service/',service,name = 'service'),
    path('contact/',contact,name = 'contact'),
]