from django import forms
from .models import Restaurante
class RestaurantCreateForm(forms.ModelForm):
    class Meta:
        model = Restaurante

        fields = [
            'name',
            'owner',
            'address',
            'phone',
            'time',
        ]

        labels = {
            'name' : 'nombre',
            'owner' : 'dueño',
            'address': 'direccion',
            'phone': 'telefono',
            'time': 'Antiguedad',
        }

        widgets = {
            'name' : forms.TextInput(),
            'owner' : forms.TextInput(),
            'address': forms.TextInput(),
            'phone':forms.NumberInput(),
            'time':forms.DateTimeInput()
        }