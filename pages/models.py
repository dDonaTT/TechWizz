from django.db import models

# Create your models here.

class Team(models.Model):
    emri = models.CharField(max_length=255)
    mbiemri = models.CharField(max_length=255)
    pozita = models.CharField(max_length=255)
    fotografia = models.ImageField(upload_to='foto/%Y/%m/%d/')


    def __str__(self):
        return self.emri
