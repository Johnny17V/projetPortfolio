from django.db import models

# Create your models here.

class Tags(models.Model):
    name = models.CharField(max_length=50)
    icon_class = models.CharField(max_length = 50, blank = True, help_text="Class Font Awesome")
    
    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
    

class ProjetModel(models.Model):
    Description = models.TextField()
    titre = models.CharField(max_length=100)
    lienGitHub = models.URLField(max_length=300, blank=True)
    imageProjet = models.ImageField(upload_to= "api/images/", blank=True, null=True)
    rapportPDF = models.FileField(upload_to = "api/rapports/", blank = True, null = True)
    lesTags = models.ManyToManyField(Tags, related_name='projets')
    
    def __str__(self):
        return f"{self.titre}"
    
    class Meta:
        verbose_name = 'Projet'
        verbose_name_plural = 'Projets'
    