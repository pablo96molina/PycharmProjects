from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'encuestas/home.html')

def signup(request):
    return HttpResponse('<h1>Signup</h1>')