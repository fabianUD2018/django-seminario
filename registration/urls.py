from django.urls import path
from .views import SignUp
app_name = 'accounts'

urlpatterns = [
    path('sign_up/', SignUp.as_view(), name='sign_up' ),
]