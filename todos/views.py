from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from .models import Todo
from .serializers import TodoSerializer, UserSerializer
from .permissions import IsOwner


# class TodoList(mixins.CreateModelMixin, generics.GenericAPIView):
#     permission_classes = [permissions.IsAuthenticated]
#     serializer_class = TodoSerializer
#     queryset = Todo.objects.all()
#
#     def get(self, request):
#         try:
#             todos = self.queryset.filter(owner=request.user)
#         except Todo.DoesNotExist:
#             todos = []
#         serializer = TodoSerializer(todos, context={'request': request}, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, *args, **kwargs):
#         print(request.user, request.data)
#         self.create(request, *args, **kwargs)

class TodoList(APIView):
    def get(self, request):
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class TodoList(generics.ListCreateAPIView):
#     queryset = Todo.objects.all()
#     serializer_class = TodoSerializer


class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAuthenticated, IsOwner)
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class UserList(generics.ListAPIView):
    # permission_classes = (permissions.IsAdminUser,)
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    # permission_classes = (permissions.IsAdminUser,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
