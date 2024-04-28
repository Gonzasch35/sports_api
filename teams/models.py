from django.db import models
from datetime import datetime

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=200)
    image = models.FileField(upload_to='gt_files')

    def __str__(self):
        return self.name
    
class Player(models.Model):
    name = models.CharField(max_length=200)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team_player')
    price = models.CharField(max_length=100, default='')
    position = models.CharField(max_length=100)
    matches = models.IntegerField(default=0)
    points = models.IntegerField(default=0)
    total_points = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Fixture(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Match(models.Model):
    matchweek = models.ForeignKey(Fixture, on_delete=models.CASCADE, related_name='match_fixture')
    local = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='local_team')
    visitante = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='visitor_team')
    match_day = models.DateTimeField(null=True, default=datetime.today())
    state = models.BooleanField(default=False)