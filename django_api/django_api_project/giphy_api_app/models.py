from django.db import models

# Create your models here.
from django.db import models

class GiphyData(models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=2083)
    
    def __str__(self):
        return self.name