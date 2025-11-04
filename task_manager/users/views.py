from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from .form import CustomUserForm, CustomAuthenticationForm, CustomUserUpdateForm
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from task_manager.tasks.models import Task

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
    
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        # Если пользователь используется в задачах, не показываем подтверждение
        in_use = (
            hasattr(self.object, 'created_task') and self.object.created_task.exists()
        ) or (
            hasattr(self.object, 'executed_tasks') and self.object.executed_tasks.exists()
        ) or Task.objects.filter(author=self.object).exists() or Task.objects.filter(executor=self.object).exists()
        if in_use:
            messages.error(request, 'Невозможно удалить пользователя, потому что он используется')
            return redirect('users')
        # Иначе показываем страницу подтверждения даже если это сам пользователь
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        messages.success(request, 'Пользователь успешно удален')
        return super().post(request, *args, **kwargs)



class UserUpdate(UpdateView):
    model = User
    template_name = 'users/update_user.html'
    form_class = CustomUserUpdateForm
    success_url = reverse_lazy('users')

    def form_valid(self, form):
        response = super().form_valid(form)
        if form.cleaned_data.get('password1'):
            update_session_auth_hash(self.request, self.object)
        messages.success(self.request, 'Пользователь успешно изменен')
        return response
