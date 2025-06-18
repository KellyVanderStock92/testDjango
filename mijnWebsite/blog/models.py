from django.conf import settings
from django.db import models
from django.utils import timezone
# Create your models here.
# dit bestanddeel van de code is verantwoordelijk voor het maken van de database tabellen en de structuur van de blog posts
# het is een model dat de structuur van de blog posts definieert
# Het model bevat de velden die een blog post moet hebben
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    # methode om de post te publiceren
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    # methode om de string representatie van de post te krijgen   
    def __str__(self):
        return self.title

