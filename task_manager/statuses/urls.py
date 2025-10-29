from django.shortcuts import render
from django.urls import path
from task_manager.statuses.views import ViewStatus , CreateStatus , UpdateStatus, DeleteStatus


urlpatterns = [
    path('', ViewStatus.as_view(), name='statuses'),
    path('create/',CreateStatus.as_view(), name='create_status'),
    path('<int:pk>/update/',UpdateStatus.as_view(), name='update'),
    path('<int:pk>/delete/', DeleteStatus.as_view(), name='delete'),
]
# Create your views here.
