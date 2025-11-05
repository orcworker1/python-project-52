from django.conf import settings
from django.db import models
from task_manager.statuses.models import Status
from django.contrib.auth.models import User
from task_manager.labels.models import Labels
import django_filters

"""""
class Task(models.Model):
    name = models.CharField(max_length=255, unique=True )
    description = models.CharField(blank=True, max_length=300)
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    executor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='executed_tasks')
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='created_task')
    labels = models.ManyToManyField(Labels, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['id']
    def __str__(self):
        return self.name
"""""

class Task(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    status = models.ForeignKey(Status, on_delete=models.PROTECT,
                               related_name="tasks")
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="created_tasks",
    )
    executor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="executed_tasks",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    labels = models.ManyToManyField(Labels, related_name="labeled_tasks",
                                    blank=True)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.name


class TaskFilter(django_filters.Filter):
    pass



# Create your models here.
