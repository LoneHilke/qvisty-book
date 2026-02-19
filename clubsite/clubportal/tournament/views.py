from django.shortcuts import render, redirect
from .models import Tournament, Match
from .forms import MatchForm, TournamentForm
from django.shortcuts import get_object_or_404




def tournament_home(request):
    return render(request, "tournament/home.html")

def tournament_list(request):
    tournaments = Tournament.objects.order_by("start_date")
    return render(request, "tournament/tournament_list.html", {"tournaments": tournaments})

def add_match(request):
    if request.method == "POST":
        form = MatchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = MatchForm()

    return render(request, "add_match.html", {"form": form})

def add_tournament(request):
    if request.method == "POST":
        form = TournamentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("tournament_list")
    else:
        form = TournamentForm()


    return render(request, "tournament/add_tournament.html", {"form": form})

def edit_tournament(request, pk):
    tournament = get_object_or_404(Tournament, pk=pk)
    if request.method == "POST":
        form = TournamentForm(request.POST, instance=tournament)
        if form.is_valid():
            form.save()
            return redirect("tournament_list")
    else:
        form = TournamentForm(instance=tournament)

    return render(request, "tournament/edit_tournament.html", {"form": form, "tournament": tournament})

def delete_tournament(request, pk):
    tournament = get_object_or_404(Tournament, pk=pk)
    if request.method == "POST":
        tournament.delete()
        return redirect("tournament_list")
    return render(request, "tournament/delete_tournament.html", {"tournament": tournament})

def tournament_detail(request, pk):
    tournament = get_object_or_404(Tournament, pk=pk)
    rounds = tournament.rounds.all()
    return render(request, "tournament/tournament_detail.html", {"tournament": tournament, "rounds": rounds})