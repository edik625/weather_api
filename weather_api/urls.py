from django.urls import path, include
from .views import WeatherViewset
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r"", WeatherViewset)

urlpatterns = [
    path('weather/<str:city>/', include(router.urls))
]
