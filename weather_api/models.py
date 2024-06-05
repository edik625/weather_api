from django.db import models
import requests 
# Create your models here.

class Weather(models.Model):
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    description = models.CharField(max_length=50,blank=False)
    temperature = models.FloatField(blank=False)


    def __str__(self):
        return self.city

    # def __str__ (self) :
    #     API_KEY = "c8b49cf6d5f9afe3b08307e6b88f185d"
    #     CITY = "rome"
    #     URL = f'http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}'
    #     response = requests.get(URL)
    #     dat = response.json()
