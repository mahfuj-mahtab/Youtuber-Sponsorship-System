from django.urls import path,include

from . import views
from youtubers.views import *
urlpatterns = [
    path('',youtubers,name = 'youtubers'),
    path('<int:id>/',youtubers_details,name = 'youtubers details'),
    path('search',searchfunc,name = 'search'),
    path('tinymce/', include('tinymce.urls')),

]