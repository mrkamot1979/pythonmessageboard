from django.db import models

# Create your models here.

#class below essentially builds a table with the textfield "models"
class Post(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text[:50]