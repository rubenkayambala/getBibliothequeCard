from django import forms
from .models import Carte

class CarteForm(forms.ModelForm):
    class Meta:
        model = Carte
        fields = [
            'nom', 'postnom', 'prenom', 'email', 'sexe', 'telephone', 'date_naissance', 'lieu_naissance', 'adresse', 'photo',
            'promotion', 'annee_academique', 'nom_pere', 'contact_pere', 'nom_mere', 'contact_mere', 'nom_tuteur', 'contact_tuteur',
            'nom_urgence', 'contact_urgence', 'filiere',
        ]
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'postnom': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'email': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'sexe': forms.Select(attrs={'class': 'form-control mb-3'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'date_naissance': forms.DateInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Ex: 12/05/2001'}),
            'adresse': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'filiere': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'promotion': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'photo': forms.FileInput(attrs={'class': 'form-control mb-3'}),

            'lieu_naissance': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'annee_academique': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'nom_pere': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'contact_pere': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'nom_mere': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'contact_mere': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'nom_tuteur': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'contact_tuteur': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'nom_urgence': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'contact_urgence': forms.TextInput(attrs={'class': 'form-control mb-3'}),
        }
        