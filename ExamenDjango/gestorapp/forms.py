from django.forms import ModelForm,EmailInput
from gestorapp.models import *
class PersonaForm(ModelForm):
    class Meta:
        model = Persona
        fields= '__all__'
        widgets={
            'email': EmailInput(attrs={'type':'email'})
        }

class CarroForm(ModelForm):
    class Meta:
        model = Carro
        fields= '__all__'


class PistaForm(ModelForm):
    class Meta:
        model = Pista
        fields= '__all__'
