from django.db import models
from django.utils.text import slugify

class Team(models.Model):
    name = models.CharField(max_length=100)
    coach = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Player(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="players")
    position = models.CharField(max_length=50, blank=True)
    number = models.PositiveIntegerField(blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def save(self, *args, **kwargs):
            if not self.slug:
                self.slug = slugify(f"{self.first_name}-{self.last_name}")
            super(Player, self).save(*args, **kwargs)  
