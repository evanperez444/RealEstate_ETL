import requests
import json
import sys

def fetch_market_trends(property_url):
    url = "https://us-real-estate-listings.p.rapidapi.com/property/marketTrends"
    querystring = {"property_url": property_url}
    headers = {
        "x-rapidapi-key": "1786a3e632msh2663eeb7333ff7ep1d4159jsnf1cbf8553e96",  # Replace with your actual key
        "x-rapidapi-host": "us-real-estate-listings.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    
    if response.status_code == 200:  # Check if the request was successful
        data = response.json()
        print(data)
        return data  # Return the JSON data
    else:
        return None  # Return None or handle the error as needed


fetch_market_trends("https://www.realtor.com/realestateandhomes-detail/2433-S-Ramona-Cir_Tampa_FL_33612_M56257-22633")