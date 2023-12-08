from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("<html><head><title>Things</title></head><body><h1>Things</h1></body></html>")
