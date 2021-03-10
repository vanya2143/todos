from django.urls import path

from .views import TodoList, TodoDetail, UserList, UserDetail, ApiRoot

urlpatterns = [
    path('', ApiRoot.as_view(), name='api-root'),

    path('users/', UserList.as_view(), name='user-list'),
    path('users/<int:pk>', UserDetail.as_view(), name='user-detail'),

    path('todos/', TodoList.as_view(), name='todo-list'),
    path('todos/<int:pk>', TodoDetail.as_view(), name='todo-detail'),
]
