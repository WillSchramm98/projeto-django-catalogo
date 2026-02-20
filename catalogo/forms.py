from django import forms
from .models import Tema, Recurso


class TemaForm(forms.ModelForm):
    class Meta:
        model = Tema
        fields = '__all__'


class RecursoForm(forms.ModelForm):
    class Meta:
        model = Recurso
        fields = '__all__'