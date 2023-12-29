from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .models import Player
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

def logout_view(request):
    logout(request)
    return redirect('login')

def login_view(request):
  context = {
    "login_view": "active"
  }
  if request.method == "POST":
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
      # Add your code below:
      login(request, user)
      return redirect("home")
    else:
      return HttpResponse("invalid credentials")
  return render(request, "registration/login.html", context)
    
@login_required
def home(request):
    return render(request, "blackjack/home.html")

@login_required
def game(request):
    return render(request, "blackjack/game.html")

class PlayerList(LoginRequiredMixin,ListView):
    model = Player
    template_name = "blackjack/player_list.html"
