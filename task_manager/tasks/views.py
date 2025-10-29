from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm

from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .form import TaskForm
from django.contrib import messages

from task_manager.tasks.models import Task

class ViewTasks(ListView):
    model = Task
    template_name = 'tasks/tasks.html'
    context_object_name = 'tasks'

class CreateTask(CreateView):
    model = Task
    template_name = 'tasks/create.html'
    form_class = TaskForm
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class UpdateTask(UpdateView):
    model = Task
    template_name = 'tasks/update.html'
    fields = ['name','description','status','executor','labels']
    success_url = reverse_lazy('tasks')

# Create your views here.
