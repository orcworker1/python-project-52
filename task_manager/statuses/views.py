from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from .form import StatusForm
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from .models import Status


class ViewStatus(ListView):
    model = Status
    template_name = 'statuses/status.html'
    context_object_name = 'statuses'

class CreateStatus(CreateView):
    model = Status
    template_name = 'statuses/created.html'
    form_class = StatusForm
    success_url = reverse_lazy('statuses')

    def post(self, request, *args, **kwargs):
        messages.success(request, 'Статус успешно создан')
        return super().post(request, *args, **kwargs)

class UpdateStatus(UpdateView):
    model = Status
    template_name = 'statuses/update.html'
    fields = ['name']
    success_url = reverse_lazy('statuses')

    def form_valid(self, form):
        messages.success(self.request, 'Статус успешно изменен')
        return super().form_valid(form)


class DeleteStatus(DeleteView):
    model = Status
    template_name = 'statuses/delete.html'
    success_url = reverse_lazy('statuses')

    def post(self, request, *args, **kwargs):
        messages.warning(request, 'Статус удалён')
        return super().post(request, *args, **kwargs)

