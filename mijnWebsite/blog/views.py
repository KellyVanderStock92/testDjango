from django.shortcuts import render

# Create your views here.

#schrijf een fuunctie die de waarden van de post_list view teruggeeft
def post_list(request):
    return render(request, 'blog/post_list.html', {}) # template post_list.html wordt gerenderd en wordt opgevuld met de inhoud, dit wordt dan aan bezoeker getoond als mooie pagina


