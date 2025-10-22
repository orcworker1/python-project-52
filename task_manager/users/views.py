from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

class ViewUsers(ListView):
    model = User
    template_name = 'templates/users_list.html'
    context_object_name = 'users'

class CreateUser(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'users/create.html'
    success_url = reverse_lazy('/')

class UserLoginView(LoginView):
    template_name = 'users/login.html'
    redirect_authenticated_user = False
    next_page = '/'

class UserLogoutView(LogoutView):
    next_page = 'login'


