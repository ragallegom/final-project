from django.db import models

# Create your models here.
class Nltk(models.Model):

    multiplication = 'multiplication'
    division = 'division'
    addition = 'addition'
    subtraction = 'subtraction'
    equality = 'equality'
    stop_words = 'stop_words'
    
    CORPUS = [
        (multiplication, 'MULTIPLICATION'),
        (division, 'DIVISION'),
        (addition, 'ADDITION'),
        (subtraction, 'SUBTRACTION'),
        (equality, 'EQUALITY'),
        (stop_words, 'STOP_WORDS'),
    ]

    corpus = models.CharField(max_length=50)
    description = models.TextField()
    corpus_type = models.CharField(
        max_length=25,
        choices=CORPUS,
        default=stop_words,
    )