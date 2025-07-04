from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)

#deze code maakt een formulier aan voor het Post model, met de velden title en text.
# Het formulier kan worden gebruikt in de views om nieuwe posts aan te maken of bestaande posts te bewerken.
# Het formulier wordt gebruikt in de templates om de velden weer te geven en om gegevens van de gebruiker te verzamelen.
# Het formulier kan worden weergegeven in de templates met behulp van de {{ form }} variabele.
# Het formulier kan worden gevalideerd en opgeslagen in de database met behulp van de save() methode.
# Het formulier kan worden gebruikt in de views om nieuwe posts aan te maken of bestaande posts te bewerken.

# Mu moet je base.html aanpassen met een link voor het bezoeken van het nieuwe blogbericht 
