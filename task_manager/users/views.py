from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from .form import CustomUserForm, CustomAuthenticationForm, CustomUserUpdateForm
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages

class ViewUsers(ListView):
    model = User
    template_name = 'users/users_list.html'
    context_object_name = 'users'

class CreateUser(CreateView):
    model = User
    template_name = 'users/create.html'
    form_class = CustomUserForm
    success_url = reverse_lazy('login')
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Пользователь успешно зарегистрирован')
        return response


class UserLoginView(LoginView):
    template_name = 'users/login.html'
    redirect_authenticated_user = True
    form_class = CustomAuthenticationForm
    def get_success_url(self):
        return reverse_lazy('index')
    def form_valid(self, form):
        messages.success(self.request,'Вы залогинены')
        return super().form_valid(form)

class UserLogoutView(LogoutView):
    http_method_names = ['get', 'post']

    def get(self, request, *args, **kwargs):
        messages.info(request, 'Вы разлогинены')
        return super().post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('index')

class UserDelete(DeleteView):
    model = User
    template_name = 'users/delete_user.html'
    success_url = reverse_lazy('users')
    
    def post(self, request, *args, **kwargs):
        messages.success(request, 'Пользователь успешно удалён')
        return super().post(request, *args, **kwargs)


class UserUpdate(UpdateView):
    model = User
    template_name = 'users/update_user.html'
    form_class = CustomUserUpdateForm
    success_url = reverse_lazy('users')

    def form_valid(self, form):
        messages.success(self.request, 'Пользователь успешно изменен')
        return super().form_valid(form)
