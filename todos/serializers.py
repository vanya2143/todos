from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Todo
        fields = ['id', 'title', 'body', 'done', 'owner', 'url', 'created']


class UserSerializer(serializers.ModelSerializer):
    todos = serializers.HyperlinkedRelatedField(
        many=True,
        view_name='todo-detail',
        read_only=True,
    )

    class Meta:
        model = User
        fields = ['id', 'username', 'url', 'todos']
