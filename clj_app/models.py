from django.db import models

class Category(models.Model):
    name = models.CharField(max_length = 255, blank = False)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length = 255, blank = False)
    description = models.CharField(max_length = 255)
    author = models.CharField(max_length = 255)
    genre = models.ForeignKey(Post, on_delete = models.CASCADE, default = 1)

    def __str__(self):
        return self.title

class Book(models.Model):
    title = models.CharField(max_length = 255, blank = False)
    author = models.CharField(max_length = 255)
    description = models.CharField(max_length = 255)
    genre = models.ForeignKey(Genre, on_delete = models.CASCADE, default = 1)

    def __str__(self):
        return self.title