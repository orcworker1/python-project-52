from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

class ViewUsers(ListView):
    model = User
    template_name = 'temlates/user_list.html'
    context_object_name = 'users'

class CreateUser(CreateView):
    model = User
    template_name = 'temlates/create.html'
    fields = ['name','last_name','user_name','password']
    success_url = reverse_lazy('user_list')

class UserLoginView(LoginView):
    template_name = 'users/login.html'
    redirect_authenticated_user = True






