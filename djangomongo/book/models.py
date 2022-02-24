from djongo import models

# Create your models here.

class Book(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=255)
    content = models.TextField()
