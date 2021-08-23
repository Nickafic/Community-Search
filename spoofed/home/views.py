from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'spoofed.html')

def login(request):
    return render(request, 'login.html')

def create(request):
    return render(request, 'create.html')