from django.urls import path # import path uit Django.urls
from . import views # import views uit de huidige map
# urlpatterns is een lijst van url patronen die de views aanroepen
urlpatterns = [
    path('', views.post_list, name='post_list'),  # de post_list view wordt aangeroepen wanneer de root url wordt bezocht
    path('post/<int:pk>/', views.post_detail, name='post_inhoud'),  # de post_detail view wordt aangeroepen wanneer een specifieke post wordt bezocht
    path('post/nieuw/', views.post_nieuw, name ='post_nieuw'),  # de post_nieuw view wordt aangeroepen wanneer de gebruiker een nieuw bericht wil aanmaken. Hierna nieuwe view toevoegen in views.py
    path('delete/<int:pk>/', views.delete_post, name='delete'),  # de delete_post view wordt aangeroepen wanneer de gebruiker een bestaand bericht wil verwijderen. Hierna nieuwe view toevoegen in views.py
]