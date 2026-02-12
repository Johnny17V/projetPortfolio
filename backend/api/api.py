from .models import Tags, ProjetModel, ReseauSociaux, Experience, Skill
from .serializers import TagsSerialiser, ProjetModelSerialiser, ReseauSociauxSerialiser, ExperienceSerialiser, SkillSerialiser
from rest_framework.response import Response
from rest_framework import viewsets


class TagsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tags.objects.all()
    serializer_class = TagsSerialiser
    
class ProjetModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ProjetModel.objects.all()
    serializer_class = ProjetModelSerialiser
    
class ReseauSociauxViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ReseauSociaux.objects.all()
    serializer_class = ReseauSociauxSerialiser
    
class ExperienceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerialiser
    
class SkillViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerialiser