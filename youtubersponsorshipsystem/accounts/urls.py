from django.urls import path,include

from . import views
from accounts.views import *
urlpatterns = [
    path('login/',login,name = 'login'),
    path('register/',register,name = 'register'),
    path('logout/',logout_user,name = 'logout user'),
    path('dashboard/',dashboard,name = 'dashboard'),
]