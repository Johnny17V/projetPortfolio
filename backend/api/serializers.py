from rest_framework import serializers
from .models import Tags, ProjetModel, ReseauSociaux, Experience, Skill

class TagsSerialiser(serializers.Serializer):
    
    class Meta:
        model = Tags
        fields = "__all__"
        
class ProjetModelSerialiser(serializers.Serializer):
    
    class Meta:
        model = ProjetModel
        fields = "__all__"

class ReseauSociauxSerialiser(serializers.Serializer):
    
    class Meta:
        model = ReseauSociaux
        fields = "__all__"
        
class ExperienceSerialiser(serializers.Serializer):
    
    class Meta:
        model = Experience
        fields = "__all__"
        
class SkillSerialiser(serializers.Serializer):
    
    class Meta:
        model = Skill
        fields = "__all__"