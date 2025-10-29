
from django.urls import path
from task_manager.tasks.views import ViewTasks, CreateTask, UpdateTask, DeleteTask

urlpatterns = [
    path('', ViewTasks.as_view(), name='tasks'),
    path('created/',CreateTask.as_view(),name='create_task'),
    path('<int:pk>/update', UpdateTask.as_view(),name='update_task'),
    path('<int:pk>/delete', DeleteTask.as_view(),name='delete_task'),
]
# Create your views here.
