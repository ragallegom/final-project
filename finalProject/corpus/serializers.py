from rest_framework import serializers

class corpusSerializer(serializers.Serializer):
    corpus = serializers.CharField(max_length=256)
    