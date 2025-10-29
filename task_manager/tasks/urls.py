
from django.urls import path
from task_manager.tasks.views import ViewTasks, CreateTask

urlpatterns = [
    path('', ViewTasks.as_view(), name='tasks'),
    path('created/',CreateTask.as_view(),name='create_task'),
]
# Create your views here.
