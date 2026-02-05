from django.shortcuts import render, redirect,  get_object_or_404
from .forms import PlayerForm
from .models import Player

def home(request):
    return render(request, "club/home.html")



def add_player(request):
    if request.method == "POST":
        form = PlayerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = PlayerForm()

    return render(request, "add_player.html", {"form": form})

def player_list(request):
    players = Player.objects.order_by("last_name", "first_name")
    return render(request, "player_list.html", {"players": players})

def player_detail(request, slug):
    player = get_object_or_404(Player, slug=slug)
    return render(request, "player_detail.html", {"player": player})