from django import forms
from applications.persona.models import Habilidades

class NewDepartamentoForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellidos=forms.CharField(max_length=50)
    departamento=forms.CharField(max_length=50)
    shorname=forms.CharField(max_length=20)

    avatar=forms.ImageField()
    habilidades=forms.ModelMultipleChoiceField(Habilidades.objects.all())

