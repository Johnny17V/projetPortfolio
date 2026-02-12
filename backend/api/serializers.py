from rest_framework import serializers
from .models import Tags, ProjetModel, ReseauSociaux, Experience, Skill

class TagsSerialiser(serializers.ModelSerializer):
    
    class Meta:
        model = Tags
        fields = "__all__"
        
class ProjetModelSerialiser(serializers.ModelSerializer):
    les_tags = TagsSerialiser(many=True, read_only=True)
    class Meta:
        model = ProjetModel
        fields = "__all__"

class ReseauSociauxSerialiser(serializers.ModelSerializer):
    
    class Meta:
        model = ReseauSociaux
        fields = "__all__"
        
class ExperienceSerialiser(serializers.ModelSerializer):
    
    class Meta:
        model = Experience
        fields = "__all__"
        
class SkillSerialiser(serializers.ModelSerializer):
    
    class Meta:
        model = Skill
        fields = "__all__"