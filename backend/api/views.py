
# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import *
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

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