

import django_filters as df

from .models import Task , Labels , Status, User


class TaskFilter(df.FilterSet):
    labels = df.ModelChoiceFilter(queryset=Labels.objects.all())
    status = df.ModelChoiceFilter(queryset=Status.objects.all())
    executor = df.ModelChoiceFilter(queryset=User.objects.all())

    class Meta:
        model = Task
        fields = ['name', 'status', 'executor', 'author', 'created_at']