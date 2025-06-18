from django.shortcuts import render
from django.utils import timezone # importeer render en timezone uit Django.shortcuts en Django.utils
from .models import Post #importeer het Post model uit de models.py file
# Create your views here.

#schrijf een fuunctie die de waarden van de post_list view teruggeeft
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date') # haal alle posts op die gepubliceerd zijn en sorteer ze op de publicatiedatum
    return render(request, 'blog/post_list.html', {'posts':posts}) # template post_list.html wordt gerenderd en wordt opgevuld met de inhoud, dit wordt dan aan bezoeker getoond als mooie pagina
#de query die we hebben geschreven vertegenwoordigt een verzameling van Post objecten uit de database die voldoen aan de filtercriteria: publicatiedatum


