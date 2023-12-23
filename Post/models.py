from datetime import datetime

from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)


class Author(models.Model):
    name = models.CharField(max_length=255)
    bio = models.CharField(max_length=255)


class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.CharField(max_length=1000000)
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, null=True, blank=True)
    author = models.ForeignKey("Author", on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)


