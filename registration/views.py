from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm
from django.urls import reverse_lazy

class SignUp (CreateView):
    form_class = RegistrationForm
    template_name = 'registration/sign_up.html'
    success_url = reverse_lazy('login')
    """
    def get_succes_url(self):
        return reverze_lazy(login)+"?registered"

        {% if 'register' in request.GET %}
        """




