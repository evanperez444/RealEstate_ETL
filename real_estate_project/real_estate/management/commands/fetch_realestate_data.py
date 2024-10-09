from django.core.management.base import BaseCommand
from your_app.models import RealEstateData
import requests

class Command(BaseCommand):
    help = 'Fetch real estate data and store it in the database'

    def add_arguments(self, parser):
        parser.add_argument('property_url', type=str, help='The URL of the property to fetch data for')

    def handle(self, *args, **kwargs):
        property_url = kwargs['property_url']

        url = "https://us-real-estate-listings.p.rapidapi.com/property/marketTrends"
        querystring = {"property_url": property_url}
        headers = {
            "x-rapidapi-key": "1786a3e632msh2663eeb7333ff7ep1d4159jsnf1cbf8553e96",  # Replace with your actual key
            "x-rapidapi-host": "us-real-estate-listings.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)

        if response.status_code == 200:
            data = response.json()

            # Extract relevant fields from the API response (you can adjust this based on the actual data structure)
            median_price = data.get('median_price')
            days_on_market = data.get('days_on_market')
            average_price_per_sqft = data.get('average_price_per_sqft')

            # Save the data to the database
            RealEstateData.objects.create(
                property_url=property_url,
                median_price=median_price,
                days_on_market=days_on_market,
                average_price_per_sqft=average_price_per_sqft
            )

            self.stdout.write(self.style.SUCCESS(f"Data fetched and saved for {property_url}"))
        else:
            self.stdout.write(self.style.ERROR(f"Failed to fetch data for {property_url}"))
