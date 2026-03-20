from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.

class Profile(AbstractUser):
    # Tes champs personnalisés directement intégrés
    bio = models.CharField(max_length=255, blank=True, null=True)
    photo = models.ImageField(upload_to="api/images_user/", blank=True, null=True)
    telephone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        # On retourne le pseudo par défaut pour l'affichage
        return self.username
    
class Tags(models.Model):
    name = models.CharField(max_length=50, unique=True)
    icon_class = models.CharField(max_length = 50, blank = True, help_text="Class Font Awesome")
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True,related_name="Tags_Personnelles")
    
    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
    

class ProjetModel(models.Model):
    description = models.TextField()
    titre = models.CharField(max_length=100)
    lien_gitHub = models.URLField(max_length=300, blank=True)
    image_Projet = models.ImageField(upload_to= "api/images_projets/", blank=True, null=True)
    rappor_PDF = models.FileField(upload_to = "api/rapports/", blank = True, null = True)
    les_tags = models.ManyToManyField(Tags, related_name='projets')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True,related_name="Projets_Personnelles")
    
    def __str__(self):
        return f"{self.titre}"
    
    class Meta:
        verbose_name = 'Projet'
        verbose_name_plural = 'Projets'
    
class ReseauSociaux(models.Model):
    name = models.CharField(max_length=50)
    icon_reseau = models.CharField(max_length=100, help_text="Class font awesome Reseau")
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True,related_name="Sociaux_Personnelles")
    lien = models.URLField(max_length=200)
    
    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name = 'reseau social'
        verbose_name_plural = 'reseau sociaux'
        
class Experience(models.Model):
    poste = models.CharField(max_length=150)
    entreprise = models.CharField(max_length=150)
    date_debut = models.DateField()
    date_fin = models.DateField(null = True, blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True,related_name="Expériences_Personnelles")
    description_taches = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.poste}"
    
    class Meta:
        verbose_name = 'Expérience'
        verbose_name_plural = 'Expériences'

class Skill(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True,related_name="Skills_Personnelles")
    
    
    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'