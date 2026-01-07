from django.db import models

class Exercice(models.Model):
   category = models.CharField(max_length=50)  # enum
   level = models.CharField(max_length=20)  # enum
   equipments = models.CharField(max_length=20)  # enum
   image_url = models.URLField()
   body_parts = models.CharField(max_length=50)  # enum
   target_muscles = models.CharField(max_length=50)  # enum
   secondary_muscles = models.CharField(max_length=50)  # enum

