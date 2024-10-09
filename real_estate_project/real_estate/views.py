from django.shortcuts import render

from django.http import JsonResponse
from .etl import fetch_realestate_data  # Assuming this function is in the etl.py file

def fetch_and_store_realestate_data(request):
    # Fetch and store real estate data
    property_url = request.GET.get('property_url', 'https://www.realtor.com/realestateandhomes-detail/2433-S-Ramona-Cir_Tampa_FL_33612_M56257-22633')
    data = fetch_realestate_data(property_url)
    if data:
        return JsonResponse({'message': 'Data fetched and stored successfully', 'data': data})
    else:
        return JsonResponse({'error': 'Failed to fetch data'}, status=500)
