from django.urls import path # import path uit Django.urls
from . import views # import views uit de huidige map
# urlpatterns is een lijst van url patronen die de views aanroepen
urlpatterns = [
    path('', views.post_list, name='post_list'),  # de post_list view wordt aangeroepen wanneer de root url wordt bezocht
]