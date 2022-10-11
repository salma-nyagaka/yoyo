from django.urls import reverse
from rest_framework.test import APIClient
from django.test import TestCase
from django.conf import settings


class BaseTestCase(TestCase):
    """Base test file to be used by other test files in the project"""

    def setUp(self):
        key = settings.API_KEY

        self.client = APIClient()

        self.locations_api_url = reverse("locations:weather-api", args=["Nairobi"])

        self.params = {
            "key": "0873153d0367435db6a113510221010",
            "q": "Nairobi",
            "days": "3",
        }

        self.no_days_in_params = {
            "q": "Nairobi",
        }
