from django.urls import path, include
from .views import WeatherViewset
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r"weather", WeatherViewset)

urlpatterns = [
    path('', include(router.urls))
]
