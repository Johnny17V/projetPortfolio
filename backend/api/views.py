
# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth import login as auth_login
from .forms import InfoGenericForm, MotDePasseForm
from django.contrib.auth import get_user_model

def showcase_view(request):
    profiles = Profile.objects.filter(is_superuser=False)
    
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




class ProjetListView(LoginRequiredMixin, ListView):
    model = ProjetModel
    template_name = 'api/projet.html' 
    context_object_name = 'projets'

    def get_queryset(self):
        return ProjetModel.objects.filter(owner=self.request.user)

class ExperienceListView(LoginRequiredMixin, ListView):
    model = Experience
    template_name = 'api/dashboard_experience.html'
    context_object_name = 'experiences'
    
    def get_queryset(self):
        return Experience.objects.filter(owner=self.request.user)
    
    
class SkillListView(LoginRequiredMixin, ListView):
    model = Skill
    template_name = 'api/dashboard_skills.html'
    context_object_name = 'skills'
    
    def get_queryset(self):
        return Skill.objects.filter(owner=self.request.user)
    
class TagsListView(LoginRequiredMixin, ListView):
    model = Tags
    template_name = "api/dashboard_tags.html"
    context_object_name = 'tags'
    
    def get_queryset(self):
        return Tags.objects.filter(owner=self.request.user)
    
class ReseauxListView(LoginRequiredMixin, ListView):
    model = ReseauSociaux
    template_name = "api/dashboard_reseaux.html"
    context_object_name = 'reseaux'
    
    def get_queryset(self):
        return ReseauSociaux.objects.filter(owner=self.request.user)
    
    
    
# 2. CREATE : Créer
class ProjetCreateView(LoginRequiredMixin, CreateView):
    model = ProjetModel
    template_name = 'api/createOrUpdateProjet.html'
    fields = ['titre', 'description', 'lien_gitHub', 'image_Projet', 'rappor_PDF', 'les_tags']
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class ExperienceCreateView(LoginRequiredMixin, CreateView):
    model = Experience
    template_name = 'api/createOrUpdateExperience.html'
    fields = ['poste', 'entreprise', 'date_debut', 'date_fin', 'description_taches']
    success_url = reverse_lazy('experience')
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['date_debut'].widget.input_type = 'date'
        form.fields['date_fin'].widget.input_type = 'date'
        return form
    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
    
class SkillsCreateView(LoginRequiredMixin, CreateView):
    model = Skill
    template_name = 'api/createOrUpdateSkill.html'
    fields = ['name', 'description']
    success_url = reverse_lazy('skills')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
    

class TagsCreateView(LoginRequiredMixin, CreateView):
    model = Tags
    template_name = 'api/createOrUpdateTags.html'
    fields = ['name', 'icon_class']
    success_url = reverse_lazy('tags')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
    
    
class ReseauxCreateView(LoginRequiredMixin, CreateView):
    model = ReseauSociaux
    template_name = 'api/createOrUpdateReseau.html'
    fields = ['name', 'icon_reseau', 'lien']
    success_url = reverse_lazy('reseaux')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
    
    
# 3. UPDATE : Modifier un projet existant
class ProjetUpdateView(LoginRequiredMixin, UpdateView):
    model = ProjetModel
    template_name = 'api/createOrUpdateProjet.html'
    fields = ['titre', 'description', 'lien_gitHub', 'image_Projet', 'rappor_PDF', 'les_tags']
    success_url = reverse_lazy('dashboard')

    def get_queryset(self):
        return ProjetModel.objects.filter(owner=self.request.user)



class ExperienceUpdateView(LoginRequiredMixin, UpdateView):
    model = Experience
    template_name = 'api/createOrUpdateExperience.html'
    fields = ['poste', 'entreprise', 'date_debut', 'date_fin', 'description_taches']
    success_url = reverse_lazy('experience')
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['date_debut'].widget.input_type = 'date'
        form.fields['date_fin'].widget.input_type = 'date'
        return form
    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
    
class SkillsUpdateView(LoginRequiredMixin, UpdateView):
    model = Skill
    template_name = 'api/createOrUpdateSkill.html'
    fields = ['name', 'description']
    success_url = reverse_lazy('skills') 

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
    

class TagsUpdateView(LoginRequiredMixin, UpdateView):
    model = Tags
    template_name = 'api/createOrUpdateTags.html'
    fields = ['name', 'icon_class']
    success_url = reverse_lazy('tags')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
    
    
class ReseauxUpdateView(LoginRequiredMixin, UpdateView):
    model = ReseauSociaux
    template_name = 'api/createOrUpdateReseau.html'
    fields = ['name', 'icon_reseau', 'lien']
    success_url = reverse_lazy('reseaux') 

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
    
    
# 4. DELETE : Supprimer un projet
class ProjetDeleteView(LoginRequiredMixin, DeleteView):
    model = ProjetModel
    template_name = 'api/delete.html'
    success_url = reverse_lazy('dashboard')

    def get_queryset(self):
        return ProjetModel.objects.filter(owner=self.request.user)
    
    
class SkillDeleteView(LoginRequiredMixin, DeleteView):
    model = Skill
    template_name = 'api/delete.html'
    success_url = reverse_lazy('skills')

    def get_queryset(self):
        return Skill.objects.filter(owner=self.request.user)


class ReseauDeleteView(LoginRequiredMixin, DeleteView):
    model = ReseauSociaux
    template_name = 'api/delete.html'
    success_url = reverse_lazy('reseaux')

    def get_queryset(self):
        return ReseauSociaux.objects.filter(owner=self.request.user)

class TagDeleteView(LoginRequiredMixin, DeleteView):
    model = Tags
    template_name = 'api/delete.html'
    success_url = reverse_lazy('tags')

    def get_queryset(self):
        return Tags.objects.filter(owner=self.request.user)
    
class ExperienceDeleteView(LoginRequiredMixin, DeleteView):
    model = Experience
    template_name = 'api/delete.html'
    success_url = reverse_lazy('experience')

    def get_queryset(self):
        return Experience.objects.filter(owner=self.request.user)
    
    
    





User = get_user_model()

# --- VUE ÉTAPE 1 ---
def inscription_etape_1(request):
    if request.method == 'POST':
        form = InfoGenericForm(request.POST, request.FILES)
        if form.is_valid():
            
            nouvel_utilisateur = form.save(commit=False)
            
            # 2. Sécurité : On lui met un mot de passe inutilisable temporairement
            nouvel_utilisateur.set_unusable_password() 
            nouvel_utilisateur.save()
            # 2. On range les données nettoyées dans la "Session" (le sac à dos)
            request.session['utilisateur_en_cours_id'] = nouvel_utilisateur.id
            
            return redirect('inscription_etape_2')
    else:
        # Si c'est la première visite, on affiche le formulaire vide
        form = InfoGenericForm()
        
    return render(request, 'api/etape1.html', {'form': form})

def inscription_etape_2(request):
    # Sécurité : Si l'utilisateur essaie d'aller à l'étape 2 sans passer par la 1
    user_id = request.session.get('utilisateur_en_cours_id')
    
    # Sécurité : S'il n'y a pas d'ID, c'est qu'il a sauté l'étape 1. On le renvoie en arrière.
    if not user_id:
        return redirect('createAccount')

    if request.method == 'POST':
        form = MotDePasseForm(request.POST)
        
        if form.is_valid():
            try:
                # 2. On va chercher notre utilisateur dans la base de données grâce à son ID
                utilisateur = User.objects.get(id=user_id)
                
                # 3. On lui donne enfin son vrai mot de passe définitif
                utilisateur.set_password(form.cleaned_data['password'])
                utilisateur.save()
                
                # 4. On vide le sac à dos (la session) car l'inscription est terminée
                del request.session['utilisateur_en_cours_id']
                
                # 5. On le connecte automatiquement en utilisant notre alias 'auth_login' !
                auth_login(request, utilisateur)
                
                # 6. Direction le Dashboard !
                return redirect('dashboard')
                
            except User.DoesNotExist:
                # Petite sécurité au cas où l'utilisateur aurait été supprimé entre temps
                return redirect('createAccount')
            
    else:
        form = MotDePasseForm()

    return render(request, 'api/etape2.html', {'form': form})


class GalerieProjetsListView(ListView):
    model = ProjetModel
    template_name = "api/all_projet.html"
    context_object_name = "tous_les_projets"
    
    queryset = ProjetModel.objects.all()
    
