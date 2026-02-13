from django.urls import path, include
from .api import TagsViewSet, ProjetModelViewSet, ReseauSociauxViewSet, ExperienceViewSet, SkillViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'projets', ProjetModelViewSet, basename='projets')
router.register(r'socials', ReseauSociauxViewSet, basename='Socials')
router.register(r'experiences', ExperienceViewSet, basename='experiences')
router.register(r'skills', SkillViewSet, basename='skills')




urlpatterns = [
    path('', include(router.urls))
]
