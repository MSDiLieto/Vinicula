from django import forms
from .models import Vinicula

class ViniculaForm(forms.ModelForm):
    class Meta:
        model = Vinicula
        fields = ('nomeVinicula', 'endereco', 'vinho', 'produtor')