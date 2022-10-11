import json
import os
import requests
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from django.conf import settings

from .utils import perform_computations


class WeatherDataRetrieveApiView(generics.RetrieveAPIView):
    """Class to fetch weather data"""

    def get(self, request, city_name):
        """Function to fetch weather data from
        external weather API"""
        try:
            # get number of days from days from params
            # assign 1 if days has not been passed in params
            days = request.GET.get("days", 1)

            # weather api url
            url = "http://api.weatherapi.com/v1/forecast.json"

            # parameters to pass to the weather api url
            weather_params = {
                "days": days,
                "q": city_name.capitalize(),
                "key": settings.API_KEY,
                "aqi": "no",
                "alerts": "no",
            }

            # get data from weather api
            weather_data = requests.get(url, weather_params)
            converted_data = json.loads(weather_data.content)

            # if response is successful, then proceed with the computations
            if weather_data.status_code == 200:
                response_data = perform_computations(converted_data)
                return_message = response_data
                return Response(return_message, status=status.HTTP_200_OK)

            # if response is unsuccessful, return the error from the api call
            else:
                return Response(converted_data, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
