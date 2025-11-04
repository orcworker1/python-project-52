from django.contrib.auth.models import User
from task_manager.labels.models import Labels
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .form import LabelsForm
from django.contrib import messages
from task_manager.tasks.models import Task


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

    def form_valid(self, form):
        messages.success(self.request, 'Метка успешно изменена')
        return super().form_valid(form)


class DeleteLabels(DeleteView):
    model = Labels
    template_name = 'labels/delete.html'
    success_url = reverse_lazy('labels')
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if Task.objects.filter(labels=self.object).exists():
            messages.error(request, 'Невозможно удалить метку, потому что она используется')
            return self.get(request, *args, **kwargs)
        messages.warning(request, 'Метка удалена')
        return super().post(request, *args, **kwargs)

# Create your views here.
