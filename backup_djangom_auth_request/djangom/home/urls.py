from django.urls import path
from . import views


# Create urls here

urlpatterns = [
    path('', views.homepage, name='home'),  # map home view
    path('auth_login/', views.auth_login.as_view(), name='auth_login'),
]