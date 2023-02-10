from django.urls import path,include

from . import views
from webpages.views import *
urlpatterns = [
    path('',youtubers,name = 'youtubers'),

]