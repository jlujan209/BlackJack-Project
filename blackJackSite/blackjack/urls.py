from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("game", views.game, name="game"), 
    path("player/", views.PlayerList.as_view(), name = "playerlist"),
    path("signup/", views.SignUp.as_view(), name="signup"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
]