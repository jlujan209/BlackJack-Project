from django.shortcuts import render

# Create your views here.

####Testing setup
from django.http import HttpResponse


def home(request):
    return render(request, "blackjack/home.html")

def game(request):
    return render(request, "blackjack/game.html")