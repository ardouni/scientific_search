from django.urls import path
from .views import search_view
from search import views

urlpatterns = [
    path('', search_view, name='search'),
    path('', views.home_view, name='home'),  # Route pour la page d'accueil

]
