from django.views import generic
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import SignUpForm

def custom_400_view(request):
    return render(request, 'errors/400.html')
    
def custom_403_view(request):
    return render(request, 'errors/403.html')

def custom_404_view(request):
    return render(request, 'errors/404.html')

def custom_500_view(request):
    return render(request, 'errors/500.html')