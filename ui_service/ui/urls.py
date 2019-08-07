from django.urls import path
from . import views

from django.urls import path
from . import views
urlpatterns = [
    path('', views.homepage, name='home'),
    path('homepage', views.homepage, name='homepage'),
]