from django.shortcuts import render

# Create your views here.

####Testing setup
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")