from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from .form import CustomUserForm, CustomAuthenticationForm, CustomUserUpdateForm
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.http import HttpResponseRedirect
from task_manager.tasks.models import Task
from django.db import models
from django.db.models import Exists, OuterRef, Q
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import get_user_model


User = get_user_model()


class OnlySelfMixin(UserPassesTestMixin):
    def test_func(self):
        obj = self.get_object()
        return (self.request.user.is_authenticated and
                obj.pk == self.request.user.pk)

    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            messages.error(self.request,
                           "Вы не авторизованы! Пожалуйста, войдите в систему")
            return super().handle_no_permission()
        messages.error(self.request,
                       "У вас нет разрешения на изменение другого пользователя")
        return redirect("users:list")




class ViewUsers(ListView):
    model = User
    template_name = 'users/users_list.html'
    context_object_name = 'users'

    def get_queryset(self):
        qs = super().get_queryset()
        has_tasks = Task.objects.filter(
            Q(author=OuterRef('pk')) | Q(executor=OuterRef('pk'))
        )
        return qs.annotate(in_use=Exists(has_tasks))


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
        messages.success(self.request, 'Вы залогинены')
        return super().form_valid(form)


class UserLogoutView(LogoutView):
    http_method_names = ['get', 'post']

    def get(self, request, *args, **kwargs):
        messages.info(request, 'Вы разлогинены')
        return super().post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('index')



class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = "users/delete_user.html"
    success_url = reverse_lazy("users")
    login_url = "login"

    def get(self, request, *args, **kwargs):
        user = self.get_object()
        # Если удаляет самого себя — сразу возвращаемся на список с ошибкой
        if request.user.is_authenticated and user.pk == request.user.pk:
            messages.error(request,
                           "Невозможно удалить пользователя, потому что он используется")
            return redirect("users")
        # Для остальных показываем страницу подтверждения, даже если пользователь используется
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        user = self.get_object()
        if (hasattr(user, "created_tasks") and user.created_tasks.exists()) or \
           (hasattr(user, "executed_tasks") and user.executed_tasks.exists()):
            messages.error(request,
                           "Невозможно удалить пользователя, потому что он используется")
            return redirect("users")
        messages.success(request, "Пользователь успешно удален")
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