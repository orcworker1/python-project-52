from django.urls import path
from .views import (
    ViewUsers,
    CreateUser,
    UserUpdate,
    UserDelete
)


urlpatterns = [
    path('', ViewUsers.as_view(), name='users'),
    path('create/', CreateUser.as_view(), name='create_user'),
    path('update/<int:pk>/',UserUpdate.as_view(), name='update_user'),
    path('delete/<int:pk>/',UserDelete.as_view(), name='delete_user'),

]