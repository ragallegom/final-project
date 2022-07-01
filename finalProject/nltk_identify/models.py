from django.db import models

# Create your models here.
class Nltk(models.Model):
    corpus = models.CharField(max_length=50)
    description = models.TextField()