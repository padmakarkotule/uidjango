from django.urls import path
from . import views

from django.urls import path
from . import views
urlpatterns = [
    path('', views.homepage, name='home'),
    path('iam/login/', views.login, name='login'),
    path('iam/logout/', views.logout, name='logout'),
]