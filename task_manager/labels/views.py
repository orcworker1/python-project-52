from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import (
    CreateView,
    DeleteView,
    ListView,
    UpdateView,
)

from task_manager.labels.forms import LabelCreationForm
from task_manager.labels.models import Labels
from task_manager.mixins import (
    CustomLoginRequiredMixin,
    ProtectErrorMixin,
)

URL_INDEX = 'labels:index'


class LabelListView(CustomLoginRequiredMixin, ListView):
    model = Labels
    template_name = 'labels/labels.html'
    context_object_name = 'labels'
    ordering = ['id']


class LabelCreateView(CustomLoginRequiredMixin,
                      SuccessMessageMixin,
                      CreateView):
    model = Labels
    template_name = 'labels/create.html'
    form_class = LabelCreationForm
    success_url = reverse_lazy(URL_INDEX)
    success_message = _('Label was created successfully')
    extra_context = {
        'title': _('Create label'),
        'button_name': _('Create')
    }


class LabelUpdateView(CustomLoginRequiredMixin,
                      SuccessMessageMixin,
                      UpdateView):
    form_class = LabelCreationForm
    model = Labels
    template_name = 'labels/update.html'
    success_url = reverse_lazy(URL_INDEX)
    success_message = _('Label was updated successfully')
    extra_context = {
        'title': _('Update label'),
        'button_name': _('Update')
    }


class LabelDeleteView(CustomLoginRequiredMixin,
                      SuccessMessageMixin,
                      ProtectErrorMixin,
                      DeleteView):
    template_name = 'labels/delete.html'
    model = Labels
    success_url = reverse_lazy(URL_INDEX)
    success_message = _('Label was deleted successfully')
    protected_object_url = reverse_lazy(URL_INDEX)
    protected_object_message = _(
        'Cannot delete this label because they are being used'
    )
    extra_context = {
        'title': _('Label deletion'),
        'button_name': _('Yes, delete')
    }