from django.shortcuts import render
from django.urls import path
from task_manager.statuses.views import ViewStatus , CreateStatus , UpdateStatus, DeleteStatus


urlpatterns = [
    path('', ViewStatus.as_view(), name='statuses'),
    path('create/',CreateStatus.as_view(), name='create_status'),
    path('update/<int:pk>/',UpdateStatus.as_view(), name='update_status'),
    path('delete/<int:pk>/', DeleteStatus.as_view(), name='delete_status'),
]
# Create your views here.
