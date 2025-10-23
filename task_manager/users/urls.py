from django.urls import path
from .views import (
    ViewUsers,
    CreateUser,
    UserUpdate
)


urlpatterns = [
    path('', ViewUsers.as_view(), name='users'),
    path('create/', CreateUser.as_view(), name='create'),
    path('<int:pk>/update/',UserUpdate.as_view(), name='update')

]