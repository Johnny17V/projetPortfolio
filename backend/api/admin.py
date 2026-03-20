from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Tags, ProjetModel, ReseauSociaux, Experience, Skill, Profile

class ProfileAdmin(UserAdmin):
    # On garde l'affichage par défaut de Django (pseudo, email, mdp, etc.)
    # Et on ajoute ta section avec tes nouveaux champs
    fieldsets = UserAdmin.fieldsets + (
        ('Informations Supplémentaires', {
            'fields': ('bio', 'photo', 'telephone')
        }),
    )
# Register your models here.
admin.site.register(Tags)
admin.site.register(ProjetModel)
admin.site.register(ReseauSociaux)
admin.site.register(Experience)
admin.site.register(Skill)
admin.site.register(Profile, ProfileAdmin)

