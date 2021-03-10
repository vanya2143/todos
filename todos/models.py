from django.db import models


class Todo(models.Model):
    owner = models.ForeignKey('auth.User', related_name='todos', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=250)
    done = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title
