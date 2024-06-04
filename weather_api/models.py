from django.db import models
import requests 
# Create your models here.

class Weather(models.Model):
    sity = models.CharField(max_length=50)


    def __str__(self):
        return self.sity

    # def __str__ (self) :
    #     API_KEY = "c8b49cf6d5f9afe3b08307e6b88f185d"
    #     CITY = "rome"
    #     URL = f'http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}'
    #     response = requests.get(URL)
    #     dat = response.json()
