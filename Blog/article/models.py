from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    create_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    abstract = models.CharField(max_length=500)
    tag = models.ManyToManyField(Tag)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + self.author + self.create_time + self.modified_time + self.category + self.tag
