from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("add-player/", views.add_player, name="add_player"),
    path("players/", views.player_list, name="player_list"),
    path("players/<slug:slug>/", views.player_detail, name="player_detail"),
]