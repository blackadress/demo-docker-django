from django.contrib import admin
from django.urls import path

from saludo.views import (InicioView, LoginView, SignUp, LogoutView)

app_name = 'saludo'

urlpatterns = [
    path('', InicioView.as_view(), name="inicio"),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registrar/', SignUp.as_view(), name='registrar'),
]
