from django.conf import settings
from django.db import models
from django.utils import timezone
# Create your models here.
# dit bestanddeel van de code is verantwoordelijk voor het maken van de database tabellen en de structuur van de blog posts
# het is een model dat de structuur van de blog posts definieert
# Het model bevat de velden die een blog post moet hebben

class Voetbalspelers(models.Model):
    auteur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, max_length=100)
    naam = models.CharField(max_length=200)
    club = models.CharField(max_length=200)
    datum_invoer = models.DateTimeField(default=timezone.now)
    datum_laatste_aanpassing = models.DateTimeField(auto_now=True)
    # methode om de invoer van de post op te slaan en te publiceren
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    # methode om de string representatie van de post te krijgen   
    def __str__(self):
        return self.naam