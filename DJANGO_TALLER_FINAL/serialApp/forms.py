from django import forms
from serialApp.models import Inscritos, Institucion

class FormInscritos(forms.ModelForm):
    class Meta:
        model = Inscritos
        fields = '__all__'

class FormInstitucion(forms.ModelForm):
    class Meta:
        model = Institucion
        fields = '__all__'