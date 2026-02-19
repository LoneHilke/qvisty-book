from django.urls import path
from . import views

urlpatterns = [
    path("", views.tournament_home, name="tournament_home"),
    path("list/", views.tournament_list, name="tournament_list"),
    path("add_match/", views.add_match, name='add_match'),
    path("add/", views.add_tournament, name="add_tournament"),
    path("edit/<int:pk>/", views.edit_tournament, name="edit_tournament"),
    path("delete/<int:pk>/", views.delete_tournament, name="delete_tournament"),
    path("<int:pk>/", views.tournament_detail, name="tournament_detail"),
]