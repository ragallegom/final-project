from curses.ascii import NL
from rest_framework import viewsets
from rest_framework import views
from rest_framework.response import Response

from .models import Nltk
from .serializer import NltkSerializer

class NltkViewSet(viewsets.ModelViewSet):
    queryset = Nltk.objects.all()
    serializer_class = NltkSerializer
    