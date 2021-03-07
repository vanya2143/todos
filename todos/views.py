from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from .models import Todo
from .serializers import TodoSerializer


# class TodoList(APIView):
#     def get(self, request):
#         todos = Todo.objects.all()
#         serializer = TodoSerializer(todos, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = TodoSerializer(request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TodoList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
