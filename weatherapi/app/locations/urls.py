from django.urls import include, path
from .views import WeatherDataRetrieveApiView

app_name = "locations"

urlpatterns = [
    path(
        "locations/<str:city_name>/",
        WeatherDataRetrieveApiView.as_view(),
        name="weather-api",
    ),
]
