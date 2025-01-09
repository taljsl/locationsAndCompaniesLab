from django.shortcuts import render
from rest_framework import generics
from .serializers import PlaceSerializer
from .models import Place

# Create your views here.
class PlaceList(generics.ListCreateAPIView):
    queryset = Place.objects.all().order_by('id')
    serializer_class = PlaceSerializer

class PlaceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Place.objects.all().order_by('id')
    serializer_class PlaceSerializer