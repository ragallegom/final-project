from dataclasses import field, fields
from .models import Nltk
from rest_framework import serializers

class NltkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nltk
        fields = '__all__'