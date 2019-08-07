from django.shortcuts import render, redirect
from django.utils import timezone

# Create your views here.

def homepage(request):
    return render(request, 'ui/home.html')
