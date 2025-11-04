

import django_filters as df
from django import forms
from django.contrib.auth import get_user_model
from task_manager.tasks.models import Task
from task_manager.labels.models import Labels
from task_manager.statuses.models import Status
User = get_user_model()


class TaskFilter(df.FilterSet):
    labels = df.ModelChoiceFilter(
        queryset=Labels.objects.all(),
        label='Метка',
        widget=forms.Select(attrs={'class': 'form-select'}))
    status = df.ModelChoiceFilter(
        queryset=Status.objects.all(),
        label='Статус',
        widget=forms.Select(attrs={'class':'form-select'}))
    executor = df.ModelChoiceFilter(
        queryset=User.objects.all(),
        label='Исполнитель',
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    self_tasks = df.BooleanFilter(
        label='Только свои задачи',
        method='filter_self_tasks',
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )

    class Meta:
        model = Task
        fields = ['status', 'executor', 'labels']

    def filter_self_tasks(self, queryset, name, value):
        if value:
            user = self.request.user
            return queryset.filter(author=user)
        return queryset

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Show full name if available for executor filter select
        field = self.form.fields.get('executor')
        if field is not None:
            def user_option_label(user: User) -> str:
                full_name = (user.get_full_name() or '').strip()
                return full_name if full_name else user.username
            field.label_from_instance = user_option_label
