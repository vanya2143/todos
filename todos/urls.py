from django.urls import path

from rest_framework.routers import DefaultRouter

from .views import ApiRoot, UserViewSet, TodoViewSet

router = DefaultRouter()
router.register('users', UserViewSet, basename='user')
router.register('todos', TodoViewSet, basename='todo')


urlpatterns = [
    path('', ApiRoot.as_view(), name='api-root'),
]

urlpatterns += router.urls
