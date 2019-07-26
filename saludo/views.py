from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import View

from saludo.forms import UserForm, UserLogin


# Create your views here.
class InicioView(View, LoginRequiredMixin):
    template_name = 'saludo/inicio.html'    
    def get(self, request):
        if(str(request.user) != 'AnonymousUser'):
            usuario = request.user
            context = {
                'nombres': usuario.first_name,
                'apellidos': usuario.last_name
            }
            return render(request, self.template_name, context)
        return redirect('saludo:login')

class LoginView(View):
    template_name = 'saludo/login.html'

    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('saludo:inicio')
        
        return render(request, self.template_name)

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('saludo:login')

class SignUp(View):
    form_class = UserForm
    template_name = 'saludo/registrar.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('saludo:inicio')
        
        return render(request, self.template_name, {'form': form})