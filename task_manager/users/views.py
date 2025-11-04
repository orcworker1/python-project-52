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


class UserDelete(DeleteView):
    model = User
    template_name = 'users/delete_user.html'          # твой шаблон подтверждения
    success_url = reverse_lazy('users')         # name роутa списка: должен вести на /users/

    def _in_use(self, user: User) -> bool:
        # исходя из твоей модели: author=PROTECT, executor=SET_NULL
        return Task.objects.filter(Q(author=user) | Q(executor=user)).exists()

    # ← ЛОВИМ ЛЮБОЙ МЕТОД ДО get()/post()
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        if request.method.lower() == "get" and self._in_use(self.object):
            messages.error(request, "Невозможно удалить пользователя, потому что он используется")
            return HttpResponseRedirect(self.success_url)
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # защита, если кто-то отправит POST напрямую
        self.object = self.get_object()
        if self._in_use(self.object):
            messages.error(request, "Невозможно удалить пользователя, потому что он используется")
            return HttpResponseRedirect(self.success_url)

        self.object.delete()
        messages.success(request, "Пользователь успешно удален")
        return HttpResponseRedirect(self.success_url)

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