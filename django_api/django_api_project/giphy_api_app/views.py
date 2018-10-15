from .serializer import GiphySerializer
from .models import GiphyData
from rest_framework import generics

class GiphyListCreate(generics.ListAPIView):
    queryset = GiphyData.objects.all()
    serializer_class = GiphySerializer
