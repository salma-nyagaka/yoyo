import os
import json
import pytest
from rest_framework import status
from django.conf import settings

from .base_file import BaseTestCase


class TestWeatherApi(BaseTestCase):
    """Test class for the weather API"""

    def test_fetch_weather_data(self):
        """Test to fetch weather data with correct params"""
        response = self.client.get(self.locations_api_url, self.params, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    
    def test_wrong_key(self):
        """ Test to check for response
        when wrong key is passed"""
        settings.API_KEY = 'nokey'
        response = self.client.get(self.locations_api_url, self.params, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
