from django import forms
from .models import Pais, Departamento, Municipio

class PaisForm(forms.ModelForm):
    class Meta:
        model = Pais
        fields = ['nombre', 'codigo']


class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = '__all__'

class MunicipioForm(forms.ModelForm):
    class Meta:
        model = Municipio
        fields = '__all__'