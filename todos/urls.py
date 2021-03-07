from django.urls import path, include

from .views import TodoList, TodoDetail


urlpatterns = [
    path('<int:pk>', TodoDetail.as_view(), name='todo-detail'),
    path('', TodoList.as_view(), name='todo-list'),
]
