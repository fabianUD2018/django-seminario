from django.urls import path
from .views import prueba, create_restaurant, edit_restaurant, delete_restaurant, list_restaurant
app_name ="restaurant"
urlpatterns = [
    path ("prueba/", prueba, name = "prueba"),
    path ("create/", create_restaurant, name ="create" ),
    path('edit/<int:id_restaurant>', edit_restaurant, name='edit'),
    path('delete/<int:id_restaurant>', delete_restaurant, name='delete'),
    path('list/', list_restaurant, name='list'),
]
