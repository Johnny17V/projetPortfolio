
# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import *

def showcase_view(request):
    # On récupère tous les utilisateurs (étudiants). 
    # On peut exclure les administrateurs avec filter(is_superuser=False)
    profiles = Profile.objects.filter(is_superuser=False)
    
    # On récupère tous les projets
    projets = ProjetModel.objects.all()
    
    context = {
        'profiles': profiles,
        'projets': projets
    }
    return render(request, 'api/showcase.html', context)

def unPortfolio(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    experience = Experience.objects.filter(owner__id = pk)
    skills = Skill.objects.filter(owner__id = pk)
    projets = ProjetModel.objects.filter(owner__id = pk)
    reseau = ReseauSociaux.objects.filter(owner__id = pk)
    context = {
        'profile' : profile,
        'experience' : experience,
        'skills' : skills,
        'projets' : projets,
        'reseau' : reseau
    }
    return render(request, "api/onePortfolio.html", context=context)
    
    
def login(request):
    return render(request, "api/login.html")