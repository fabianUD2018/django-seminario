from django.urls import path
from .views import create_ingrediente, delete_ingrediente, edit_ingrediente, list_ingrediente
#importar vistas basadas en clases
from .views import CreatePlatillo, ListPlatillo, DeletePlatillo, EditPlatillo

app_name = 'platillo'

urlpatterns = [
    path('ingrediente/create/', create_ingrediente, name ='ingrediente_create'),
    path ('ingrediente/edit/<int:id_ingrediente>/', edit_ingrediente, name ='ingrediente_edit'),
    path ('ingrediente/delete/<int:id_ingrediente>/', delete_ingrediente, name='ingrediente_delete'),
    path ('ingrediente/list/', list_ingrediente, name='ingrediente_list'),
    path('platillo/create/', CreatePlatillo.as_view(), name ='platillo_create'),
    path('platillo/list/', ListPlatillo.as_view(), name='platillo_list'),
    path('platilo/delete/<int:pk>/', DeletePlatillo.as_view(), name = 'platillo_delete'),
    path('platillo/edit/<int:pk>/', EditPlatillo.as_view(), name='platillo_edit'),
]
