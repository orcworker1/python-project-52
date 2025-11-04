
from django.urls import path
from task_manager.tasks.views import ViewTasks, CreateTask, UpdateTask, DeleteTask , DetailViewTask


urlpatterns = [
    path('', ViewTasks.as_view(), name='tasks'),
    path('created/',CreateTask.as_view(),name='create_task'),
    path('update/<int:pk>', UpdateTask.as_view(),name='update_task'),
    path('delete/<int:pk>', DeleteTask.as_view(),name='delete_task'),
    path('task/<int:pk>', DetailViewTask.as_view(),name='detail_view'),
]
# Create your views here.
