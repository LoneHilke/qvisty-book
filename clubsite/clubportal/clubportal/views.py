from django.shortcuts import render
from news.models import Article
from club.models import Team
from tournament.models import Match
from datetime import date

def home(request):
    latest_articles = Article.objects.order_by("-published_at")[:3]
    teams = Team.objects.all()[:3]
    #upcoming_matches = Match.objects.order_by("date")[:3]

    return render(request, "home.html", {
        "latest_articles": latest_articles,
        "teams": teams,
        #"upcoming_matches": upcoming_matches,
    })