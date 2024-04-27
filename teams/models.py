from django.db import models

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
