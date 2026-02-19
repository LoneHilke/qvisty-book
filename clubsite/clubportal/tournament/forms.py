from django import forms
from .models import Match, Tournament

class MatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = ["tournament", "home_team", "away_team", "match_date", "home_score", "away_score"]

    def clean(self):
        cleaned_data = super().clean()
        home_team = cleaned_data.get("home_team")
        away_team = cleaned_data.get("away_team")

        if home_team and away_team and home_team == away_team:
            raise forms.ValidationError(
                "A team cannot play against itself."
            )

        return cleaned_data

class TournamentForm(forms.ModelForm):
    class Meta:
        model = Tournament
        fields = ["name", "description", "start_date"]