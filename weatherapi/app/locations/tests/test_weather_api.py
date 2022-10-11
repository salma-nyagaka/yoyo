import os
import json
import pytest
from rest_framework import status

from .base_file import BaseTestCase
from django.conf import settings


class TestWeatherApi(BaseTestCase):
    """Test class for the weather API"""

    def test_fetch_weather_data(self):
        """Test to fetch weather data with correct params"""
        response = self.client.get(self.locations_api_url, self.params, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
