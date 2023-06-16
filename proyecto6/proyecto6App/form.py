from django import forms
from proyecto6App.models import Proyecto

class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = '__all__'
        widgets = {
            'fechaInicio': forms.TextInput(attrs={'type': 'date'}),
            'fechaFin': forms.TextInput(attrs={'type': 'date'}),
        }
        


