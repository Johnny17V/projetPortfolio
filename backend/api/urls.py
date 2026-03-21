from django.urls import path, include
from .api import TagsViewSet, ProjetModelViewSet, ReseauSociauxViewSet, ExperienceViewSet, SkillViewSet
from rest_framework.routers import DefaultRouter
from . import views  # <-- Import de ta nouvelle vue

router = DefaultRouter()
router.register(r'projets', ProjetModelViewSet, basename='projets')
router.register(r'socials', ReseauSociauxViewSet, basename='Socials')
router.register(r'experiences', ExperienceViewSet, basename='experiences')
router.register(r'skills', SkillViewSet, basename='skills')

urlpatterns = [
    # Ta nouvelle page vitrine sera accessible via http://localhost:8000/api/showcase/
    path('showcase/', views.showcase_view, name='showcase'),
    path('showcase/<int:pk>/', views.unPortfolio, name='portfolio'),
    
    # Tes routes API générées par le router
    path('', include(router.urls))
]