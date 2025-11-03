

import django_filters as df
from django import forms
from .models import Task , Labels , Status, User


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
