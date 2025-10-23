from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from .form import CustomUserForm
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages

class ViewUsers(ListView):
    model = User
    template_name = 'users/users_list.html'
    context_object_name = 'users'

class CreateUser(CreateView):
    model = User
    form_class = CustomUserForm
    template_name = 'users/create.html'
    success_url = reverse_lazy('login')
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Пользователь успешно зарегистрирован')
        return response

class UserLoginView(LoginView):
    template_name = 'users/login.html'
    redirect_authenticated_user = True
    def get_success_url(self):
        return reverse_lazy('index')
    def form_valid(self, form):
        messages.success(self.request,'Вы успешно авторизовались!')
        return super().form_valid(form)

class UserLogoutView(LogoutView):
    http_method_names = ['get', 'post']

    def get(self, request, *args, **kwargs):
        messages.info(request, 'Вы вышли из системы')
        return super().post(request, *args, **kwargs)

    def get_next_page(self):
        return reverse_lazy('login')


class UserUpdate(UpdateView):
    model = User
    template_name = 'users/update_user.html'
    fields = ['first_name','last_name']
    success_url = reverse_lazy('users')

    def form_valid(self, form):
        return super().form_valid(form)
