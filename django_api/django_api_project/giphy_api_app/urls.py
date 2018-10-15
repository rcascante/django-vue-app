from django.urls import path
from . import views

app_name = 'giphy-app'
urlpatterns = [
    path('list/', views.GiphyListCreate.as_view(), name='giphy-list')
]
