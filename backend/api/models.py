from django.db import models

# Create your models here.

class Tags(models.Model):
    name = models.CharField(max_length=50, unique=True)
    icon_class = models.CharField(max_length = 50, blank = True, help_text="Class Font Awesome")
    
    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
    

class ProjetModel(models.Model):
    description = models.TextField()
    titre = models.CharField(max_length=100)
    lien_gitHub = models.URLField(max_length=300, blank=True)
    image_Projet = models.ImageField(upload_to= "api/images/", blank=True, null=True)
    rappor_PDF = models.FileField(upload_to = "api/rapports/", blank = True, null = True)
    les_tags = models.ManyToManyField(Tags, related_name='projets')
    
    def __str__(self):
        return f"{self.titre}"
    
    class Meta:
        verbose_name = 'Projet'
        verbose_name_plural = 'Projets'
    
class ReseauSociaux(models.Model):
    name = models.CharField(max_length=50)
    icon_reseau = models.CharField(max_length=100, help_text="Class font awesome Reseau")
    
    class Meta:
        verbose_name = 'reseau social'
        verbose_name_plural = 'reseau sociaux'