from rest_framework import serializers
from .models import GiphyData


class GiphySerializer(serializers.ModelSerializer):
    class Meta:
        model = GiphyData
        fields = ('name', 'url')
