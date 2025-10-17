from django.urls import path
from task_manager import views


urlpatterns = [
    path('', views.index, name='/'),
    path('login/',views.login, name='login'),
]