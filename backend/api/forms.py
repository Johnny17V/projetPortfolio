from django import forms
from django.contrib.auth import get_user_model


User = get_user_model()

class InfoGenericForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'telephone', 'bio', 'photo']
        
        
class MotDePasseForm(forms.Form):
    
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Entrez votre mot de passe'}), 
        label="Mot de passe"
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirmez le mot de passe'}), 
        label="Confirmez le mot de passe"
    )
    
    def clean(self):
        cleaned_data = super().clean()
        mdp1 = cleaned_data.get("password")
        mdp2 = cleaned_data.get("confirm_password")

        if mdp1 and mdp2 and mdp1 != mdp2:
            raise forms.ValidationError("Les mots de passe ne correspondent pas !")
        return cleaned_data
