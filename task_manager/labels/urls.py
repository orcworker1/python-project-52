from django.shortcuts import render
from django.urls import path
from task_manager.labels.views import ViewLabels, CreateLabels , UpdateLabels, DeleteLabels


urlpatterns = [
    path('', ViewLabels.as_view(), name='labels'),
    path('created/', CreateLabels.as_view(), name='create_label'),
    path('<int:pk/update/', UpdateLabels.as_view(), name='update_label'),
    path('<int:pk/delete/', DeleteLabels.as_view(), name='delete_label'),
]