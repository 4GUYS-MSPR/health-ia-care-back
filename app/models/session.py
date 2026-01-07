from django.db import models


class Session(models.Model):
    max_bpm = models.IntegerField()
    avg_bpm = models.IntegerField()
    resting_bpm = models.IntegerField()
    duration = models.TimeField() 
    calories_burned = models.FloatField()
    exercices = models.TextField() #en attente
    water_intake = models.FloatField()
    member = models.ForeignKey('Member', on_delete=models.CASCADE, related_name='sessions')

   
   