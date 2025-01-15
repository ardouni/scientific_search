from django.shortcuts import render
import random
from django.shortcuts import render
from .forms import SearchForm
from .models import ScientificPaper

import random
from django.shortcuts import render
from .forms import SearchForm
from .models import ScientificPaper

# Définir la fonction gpo_search
def gpo_search(query, dataset):
    ranked_results = random.sample(dataset, len(dataset))  # Classement aléatoire (remplace par GPO réel)
    return ranked_results

# Vue pour la recherche
def search_view(request):
    form = SearchForm()
    results = []
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            papers = list(ScientificPaper.objects.all())
            results = gpo_search(query, papers)
    return render(request, 'search.html', {'form': form, 'results': results})

from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully! You can now log in.')
            return redirect('login')  # Rediriger vers la page de connexion après la création
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

# Vue de connexion
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Rediriger vers la page d'accueil après la connexion
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')
from django.contrib.auth import logout

def logout_view(request):
    logout(request)  # Déconnecte l'utilisateur
    return redirect('login') 

# Vue de la page d'accueil, accessible après connexion
@login_required
def home_view(request):
    return render(request, 'home.html')

















