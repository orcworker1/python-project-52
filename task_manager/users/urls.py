from django.urls import path
from .views import (
    ViewUsers,
    CreateUser,
    UserUpdate,
)

from task_manager.users.views import UserDelete

urlpatterns = [
    path('', ViewUsers.as_view(), name='users'),
    path('create/', CreateUser.as_view(), name='create_user'),
    path('<int:pk>/update/',UserUpdate.as_view(), name='update_user'),
    path('<int:pk>/delete/',UserDelete.as_view(), name='delete_user'),

]