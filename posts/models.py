from django.db import models

# Create your models here.

## Model class represent table in the database
class Post(models.Model):
    title = models.CharField(max_length=100)
    description  = models.TextField()
    image = models.CharField(max_length=100)
    version = models.IntegerField()
    publisher_email= models.EmailField()
    privacy = models.CharField(max_length=2, choices=[(1, 'Public'),(2, 'Private')])

