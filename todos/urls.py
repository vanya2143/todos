from django.urls import path, include

from .views import TodoList, TodoDetail, UserList, UserDetail


urlpatterns = [
    path('users/', UserList.as_view(), name='user-list'),
    path('users/<int:pk>', UserDetail.as_view(), name='user-detail'),
    path('<int:pk>', TodoDetail.as_view(), name='todo-detail'),
    path('', TodoList.as_view(), name='todo-list'),
]
