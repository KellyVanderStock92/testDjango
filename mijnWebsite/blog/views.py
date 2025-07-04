from django.shortcuts import render
from django.utils import timezone # importeer render en timezone uit Django.shortcuts en Django.utils
from django.shortcuts import render, get_object_or_404 
from .models import Post #importeer het Post model uit de models.py file
# Create your views here.

#schrijf een fuunctie die de waarden van de post_list view teruggeeft
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date') # haal alle posts op die gepubliceerd zijn en sorteer ze op de publicatiedatum
    return render(request, 'blog/post_list.html', {'posts':posts}) # template post_list.html wordt gerenderd en wordt opgevuld met de inhoud, dit wordt dan aan bezoeker getoond als mooie pagina
#de query die we hebben geschreven vertegenwoordigt een verzameling van Post objecten uit de database die voldoen aan de filtercriteria: publicatiedatum

#schrijf een functie die de waarden van de post_detail view teruggeeft
def post_detail(request, pk): # pk staat voor primary key, dit is een unieke identifier voor elk Post object
    post=get_object_or_404(Post, pk=pk) # haal het Post object op met de opgegeven primary key, als het niet bestaat, geef dan een 404 foutmelding
    return render(request, 'blog/post_inhoud.html', {'post': post}) # template post_inhoud.html wordt gerenderd en wordt opgevuld met de inhoud van het Post object, dit wordt dan aan bezoeker getoond als mooie pagina. template aanmaken in de templates/blog folder