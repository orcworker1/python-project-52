from django.db import models


class Labels(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['id']
    def __str__(self):
        return self.name

# Create your models here.
