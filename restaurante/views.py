from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RestaurantCreateForm
from .models import Restaurante
from django.urls import reverse_lazy
# Create your views here.
def prueba (request):
    
    return HttpResponse("<h1> Hola Mundo</h1")
def create_restaurant(request):
    
    if request.method =="POST":
        formulario = RestaurantCreateForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            
            return redirect("restaurant:list")
    else:
        formulario = RestaurantCreateForm()
    return render(request, 'restaurante/create.html',{'form':formulario})

def edit_restaurant(request, id_restaurant):
        restaurant = Restaurante.objects.get(pk=id_restaurant)
        formulario = RestaurantCreateForm(instance=restaurant)
        if request.method =="POST":
                formulario = RestaurantCreateForm(request.POST, instance=restaurant)
                if formulario.is_valid():
                        formulario.save()
                        return redirect("restaurant:list")
        return render(request, 'restaurante/create.html',{'form':formulario})

def delete_restaurant(request, id_restaurant):
        restaurant = Restaurante.objects.get(pk=id_restaurant)
        formulario = RestaurantCreateForm(instance=restaurant)
        if request.method =="POST":
                restaurant.delete()
                return redirect("restaurant:list")
        return render(request, 'restaurante/create.html',{'form':formulario})

def list_restaurant(request):
        restaurants = Restaurante.objects.all()
        return render (request, 'restaurante/list.html', {"rest": restaurants})