from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.routers import reverse

from .models import Todo
from .serializers import TodoSerializer, UserSerializer
from .permissions import IsOwnerOrAdmin


class ApiRoot(APIView):
    def get(self, request):
        return Response({
            'users': reverse('user-list', request=request),
            'todos': reverse('todo-list', request=request)
        })


class TodoList(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        todos = Todo.objects.all().filter(owner=request.user)
        serializer = TodoSerializer(todos, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = TodoSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated & IsOwnerOrAdmin]
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class UserList(generics.ListAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
