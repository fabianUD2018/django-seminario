from django.shortcuts import render, redirect, get_object_or_404
from .models import Ingrediente, Platillo
from .forms import IngredienteForm, PlatilloForm
from django.views.generic import CreateView, DeleteView, UpdateView, ListView
from django.urls import reverse_lazy

# Create your vsiews here.

#################################
#vistas basadas en funcion
#################################

def list_ingrediente(request):
        list = Ingrediente.objects.all()
        return render (request, 'platillo/ingrediente_list.html', {'lista':list})

def edit_ingrediente(request, id_ingrediente):
        #ingrediente = Ingrediente.objects.get(id_ingrediente)
        ingrediente = get_object_or_404(Ingrediente, pk=id_ingrediente)
        form = IngredienteForm( instance=ingrediente)
        if request.method=='POST':
            form = IngredienteForm(request.POST, instance=ingrediente)
            if form.is_valid():
                form.save()
                return redirect('platillo:ingrediente_list')
        else:           
            return render(request, 'platillo/ingrediente_form.html', {'form': form})
            
def create_ingrediente(request):
    
    if request.method=='POST':
        form = IngredienteForm(request.POST)
        if form.is_valid():
                form.save()
                return redirect("platillo:ingrediente_list")
    form = IngredienteForm()
    return render (request, "platillo/ingrediente_form.html", {'form': form})
    
def delete_ingrediente(request, id_ingrediente):
        #ingrediente = Ingrediente.objects.get(id=id_ingre)
        ingrediente = get_object_or_404(Ingrediente, pk=id_ingrediente)
        if request.method == 'POST':
            ingrediente.delete()
            return redirect("platillo:ingrediente_list")
        return render(request, 'platillo/ingrediente_delete.html', {'ingrediente':ingrediente})




################################
#vistas basadas en clases 
################################

class CreatePlatillo(CreateView):
    model = Platillo
    form_class = PlatilloForm
    template_name = "platillo/platillo_form.html"
    success_url = reverse_lazy("platillo:platillo_list")


class ListPlatillo(ListView):
    model = Platillo    
    template_name = 'platillo:platillo_list'

class DeletePlatillo(DeleteView):
    model = Platillo
    template_name ='platillo/platillo_delete.html'
    success_url = reverse_lazy('platillo:platillo_list')

class EditPlatillo(UpdateView):
    model = Platillo
    form_class = PlatilloForm
    #context_object_name 
    template_name = 'platillo/platillo_form.html'
    success_url = reverse_lazy('platillo:platillo_list')
        
                
