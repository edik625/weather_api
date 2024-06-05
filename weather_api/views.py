from django.shortcuts import render
from .models import Weather
from .serializers import WeatherSerializer
from rest_framework import viewsets
from .utils import weather_api
from rest_framework.response import Response
# Create your views here.


class WeatherViewset(viewsets.ModelViewSet):
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer
    
    def create(self, request, *args, **kwargs):
        city = request.data.get('city')
        country = request.data.get('country')
        
        
        weather_data = weather_api(city)
        
        if weather_data:
            data = {
                'city': city,
                'country': country,
                'temperature': weather_data['main']['temp'],
                'description': weather_data['weather'][0]['description'],
                'wind' : weather_data['wind']['speed']
            }
            
            serializer = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)

            return Response(serializer.data)
        return Response({'error': 'City Not Found'})
