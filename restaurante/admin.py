from django.contrib import admin
from .models import Restaurante
# Register your models here.
class RestaurantAdmin(admin.ModelAdmin):
    #fields = ('name', 'owner')
    list_display = ('name', 'owner')


admin.site.register(Restaurante, RestaurantAdmin)