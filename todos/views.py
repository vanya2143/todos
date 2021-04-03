from django.contrib.auth.models import User

from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.routers import reverse

from .models import Todo
from .serializers import TodoSerializer, UserSerializer
from .permissions import IsOwnerOrAdmin


@api_view(['GET'])
def api_root(request):
    return Response({
        'auth': reverse('api-auth-root', request=request),
        'users': reverse('user-list', request=request),
        'todos': reverse('todo-list', request=request)
    })


class TodoViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated & IsOwnerOrAdmin]
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def filter_queryset(self, queryset):
        queryset = super(TodoViewSet, self).filter_queryset(queryset)
        return queryset.filter(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAdminUser,)
    queryset = User.objects.all()
