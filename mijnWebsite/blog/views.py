from django.shortcuts import render
from django.utils import timezone # importeer render en timezone uit Django.shortcuts en Django.utils
from django.shortcuts import render, get_object_or_404 
from django.shortcuts import redirect
from .models import Post #importeer het Post model uit de models.py file
from .forms import PostForm # importeer het PostForm uit de forms.py file, dit is nodig om een nieuw bericht aan te maken of een bestaand bericht te bewerken
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

#functie die redirect naar de post_list view na het opslaan van een nieuw bericht
def post_nieuw(request):
    if request.method == "POST":  # controleer of het verzoek een POST-verzoek is
        form = PostForm(request.POST)  # maak een nieuw PostForm object aan met de gegevens van het formulier
        if form.is_valid():  # controleer of het formulier geldig is
            post = form.save(commit=False)  # sla het formulier op, maar commit nog niet naar de database
            post.author = request.user
            post.published_date = timezone.now()  # stel de publicatiedatum in op de huidige tijd
            post.save()  # sla het Post object op in de database
            return redirect('post_list')  # redirect naar de post_list view
    else:
        form = PostForm()  # maak een nieuw PostForm object aan voor GET-verzoeken

    return render(request, 'blog/post_edit.html', {'form': form})  # render de template post_edit.html en geef het formulier door aan de template

#functie die een bestaand bericht verwijdert
def delete_post(request, pk):
    post_to_delete = get_object_or_404(Post, id=pk)
    if request.method == "POST":
        post_to_delete.delete()
        return redirect('post_list')  # na verwijderen terug naar lijst
    # Als iemand via GET komt: toon een bevestigingspagina (optioneel)
    return render(request, 'blog/post_bevestig_verwijderen.html', {'post': post_to_delete})