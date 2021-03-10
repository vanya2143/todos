from django.contrib.auth.models import User
from django.test import TestCase

from todos.models import Todo


class TodoModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = User.objects.create_user(username='test', password='123')
        Todo.objects.create(title='first todo', body='Todo body', owner=test_user)

    def test_title_content(self):
        todo = Todo.objects.get(id=1)
        title = f'{todo.title}'
        self.assertEqual(title, 'first todo')

    def tets_body_content(self):
        todo = Todo.objects.get(id=1)
        body = f'{todo.body}'
        self.assertEqual(body, 'Todo body')
