from django.shortcuts import render
from .models import Weather
from .serializers import WeatherSerializer
from rest_framework import viewsets
# Create your views here.


class WeatherViewset(viewsets.ModelViewSet):
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer


    