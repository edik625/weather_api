import requests
API_KEY = "c8b49cf6d5f9afe3b08307e6b88f185d"
CITY = "tbilisi"
URL = f'http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}'

response = requests.get(URL)
dat = response.json()
print(dat["main"]["temp"])
print(dat["weather"][0]["description"])
print(dat['wind']['speed'])
print(dat)
