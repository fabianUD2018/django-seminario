from django.contrib import admin
from .models import Platillo, Ingrediente

# Register your models here.
class PlatilloAdmin(admin.ModelAdmin):
    pass


class IngredienteAdmin(admin.ModelAdmin):
    pass
    
    
admin.site.register(Platillo, PlatilloAdmin)
admin.site.register(Ingrediente, IngredienteAdmin)
