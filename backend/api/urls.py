from django.urls import path, include
from .api import TagsViewSet, ProjetModelViewSet, ReseauSociauxViewSet, ExperienceViewSet, SkillViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'projets', ProjetModelViewSet, basename='projets')
urlpatterns = [
    path('', include(router.urls))
]
