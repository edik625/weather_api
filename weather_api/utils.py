import requests
from django.conf import settings


API_KEY = "c8b49cf6d5f9afe3b08307e6b88f185d"



def weather_api(CITY):
    API_KEY = settings.weather
    
    URL = f'http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}'

    response = requests.get(URL)
    # dat = response.json()
    if response.status_code == 200:
        return response.json()
    # print(dat["weather"][0]["description"])
    # print(dat)
