from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<em>Hey boi</em>")

# Create your views here.