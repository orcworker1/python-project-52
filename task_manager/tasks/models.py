from cProfile import label

from django.db import models
from task_manager.statuses.models import Status
from django.contrib.auth.models import User
from task_manager.labels.models import Labels


class Task(models.Model):
    name = models.CharField(max_length=255, unique=True )
    description = models.CharField(blank=True)
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    executor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='executed_tasks')
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='created_task')
    labels = models.ManyToManyField(Labels, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['id']
    def __str__(self):
        return self.name



# Create your models here.
