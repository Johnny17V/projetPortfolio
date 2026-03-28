from django.urls import path, include
from django.contrib.auth import views as auth_views
from .api import TagsViewSet, ProjetModelViewSet, ReseauSociauxViewSet, ExperienceViewSet, SkillViewSet
from rest_framework.routers import DefaultRouter
from . import views 


router = DefaultRouter()
router.register(r'projets', ProjetModelViewSet, basename='projets')
router.register(r'socials', ReseauSociauxViewSet, basename='Socials')
router.register(r'experiences', ExperienceViewSet, basename='experiences')
router.register(r'skills', SkillViewSet, basename='skills')

urlpatterns = [

    path('showcase/', views.showcase_view, name='showcase'),
    path('showcase/<int:pk>/', views.unPortfolio, name='portfolio'),
    path("showcase/login/", auth_views.LoginView.as_view(template_name = "api/login.html"), name="login"),

    path('', include(router.urls)),
    
    path("dashboard/profil/", views.ProjetListView.as_view(), name = 'dashboard'),
    path("dashboard/experience/", views.ExperienceListView.as_view(), name = 'experience'),
    path("dashboard/skills/", views.SkillListView.as_view(), name = 'skills'),
    path("dashboard/tags/", views.TagsListView.as_view(), name = 'tags'),
    path("dashboard/reseaux/", views.ReseauxListView.as_view(), name = 'reseaux'),
    
    path("dashboard/profil/save/", views.ProjetCreateView.as_view(), name='saveProjet'),
    path("dashboard/experience/save/", views.ExperienceCreateView.as_view(), name = 'saveExperience'),
    path("dashboard/skills/save/", views.SkillsCreateView.as_view(), name = 'saveSkills'),
    path("dashboard/tags/save/", views.TagsCreateView.as_view(), name = 'saveTags'),
    path("dashboard/reseaux/save/", views.ReseauxCreateView.as_view(), name = 'saveReseaux'),
    
    path("dashboard/profil/<int:pk>/update/", views.ProjetUpdateView.as_view(), name = 'updatedashboard'),
    path("dashboard/experience/<int:pk>/update/", views.ExperienceUpdateView.as_view(), name = 'updateexperience'),
    path("dashboard/skills/<int:pk>/update/", views.SkillsUpdateView.as_view(), name = 'updateskills'),
    path("dashboard/tags/<int:pk>/update/", views.TagsUpdateView.as_view(), name = 'updatetags'),
    path("dashboard/reseaux/<int:pk>/update/", views.ReseauxUpdateView.as_view(), name = 'updatereseaux'),
    
    path("dashboard/profil/<int:pk>/delete/", views.ProjetDeleteView.as_view(), name = 'deletedashboard'),
    path("dashboard/experience/<int:pk>/delete/", views.ExperienceDeleteView.as_view(), name = 'deleteexperience'),
    path("dashboard/skills/<int:pk>/delete/", views.SkillDeleteView.as_view(), name = 'deleteskills'),
    path("dashboard/tags/<int:pk>/delete/", views.TagDeleteView.as_view(), name = 'deletetags'),
    path("dashboard/reseaux/<int:pk>/delete/", views.ReseauDeleteView.as_view(), name = 'deletereseaux'),
]

