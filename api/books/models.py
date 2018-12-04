from django.db import models

# Create your models here.

class Book(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255, unique=True)
    author_name = models.CharField(max_length=250)
    description = models.TextField(blank=True, default='')
    price = models.DecimalField(max_digits=6, decimal_places=2)

class Chapter(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    title = models.CharField(max_length=1000)
    description = models.TextField(blank=True, default='')
    content = models.TextField(blank=False, default='content')
