from django.shortcuts import render, redirect
from django.utils import timezone

# Create your views here.

def homepage(request):
    return render(request, 'ui/home/home.html')

def login(request):
    return render(request, 'ui/IAM/login.html')

def logout(request):
    return render(request, 'ui/IAM/logout.html')
