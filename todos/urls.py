from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import api_root, UserViewSet, TodoViewSet


router = DefaultRouter()
router.register('users', UserViewSet, basename='user')
router.register('todos', TodoViewSet, basename='todo')


urlpatterns = [
    path('', api_root, name='api-root'),
]

urlpatterns += router.urls
