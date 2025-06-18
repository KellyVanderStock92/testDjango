from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls), # de admin interface van Django
    path('', include('blog.urls')),  # de urls.py uit blog wordt hier toegevoegd
]
