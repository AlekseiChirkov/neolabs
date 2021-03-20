from django.db import models
from django.contrib.auth.models import User



class Post(models.Model):
    title = models.CharField(max_length=128, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=None, blank=True, null=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title}'


class PostCategory(models.Model):
    title = models.CharField(max_length=32)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.title}'


class Author(models.Model):
    name = models.CharField(max_length=32)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.name}'
