from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from task_manager.labels.models import Labels
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .form import LabelsForm
from django.contrib import messages


class ViewLabels(ListView):
    model = Labels
    template_name = 'labels/labels.html'
    context_object_name = 'labels'

class CreateLabels(CreateView):
    model = Labels
    template_name = 'labels/created.html'
    form_class = LabelsForm
    success_url = reverse_lazy('labels')
    def post(self, request, *args, **kwargs):
        messages.success(request, 'Метка успешно создана')
        return super().post(request, *args, **kwargs)

class UpdateLabels(UpdateView):
    model = Labels
    template_name = 'labels/update.html'
    fields = ['name']
    success_url = reverse_lazy('labels')


class DeleteLabels(DeleteView):
    model = Labels
    template_name = 'labels/delete.html'
    success_url = reverse_lazy('labels')
    def post(self, request, *args, **kwargs):
        messages.warning(request, 'Метка удалена')
        return super().post(request, *args, **kwargs)

# Create your views here.
