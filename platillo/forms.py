from django import forms
from .models import Ingrediente, Platillo
class IngredienteForm(forms.ModelForm):
    class Meta:
        model = Ingrediente
        
        fields = [
            'nombre',
            'precio',
        ]

        labels = {
            'nombre': 'nombre',
            'precio': 'precio del producto',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={}),
            'precio': forms.NumberInput( attrs={})
        }


class PlatilloForm (forms.ModelForm):
    class Meta:
        
        model = Platillo
        
        fields = [
            'name',
            'precio',
            'restaurante',
            'ingredientes',
        ]

        labels = {
            'name':"nombre",
            'precio':'precio',
            'restaurante':'restaurante',
            'ingredientes':'ingredientes',
        }

        widgets = {
            'name':forms.TextInput(attrs={'placeholder':'Ingrese el nombre del platillo'}),
            'precio': forms.NumberInput(),
            'restaurante': forms.Select(),
            'ingredientes':forms.SelectMultiple(),
        }

