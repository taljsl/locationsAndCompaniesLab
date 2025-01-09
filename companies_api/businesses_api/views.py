from django.shortcuts import render
from rest_framework import generics
from .serializers import BusinessSerializer
from .models import Business
# Create your views here.

class BusinessList(generics.ListCreateAPIView):
    queryset = Business.objects.all().order_by('id')
    serializer_class = BusinessSerializer

class BusinessDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Business.objects.all().order_by('id')
    serializer_class = BusinessSerializer