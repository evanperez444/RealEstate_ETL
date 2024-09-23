import requests
import json
import sys

url = "https://us-real-estate-listings.p.rapidapi.com/property/marketTrends"

querystring = {"property_url":"https://www.realtor.com/realestateandhomes-detail/2433-S-Ramona-Cir_Tampa_FL_33612_M56257-22633"}

headers = {
	#Hide this!!!!!!!!!
	"x-rapidapi-key": "1786a3e632msh2663eeb7333ff7ep1d4159jsnf1cbf8553e96",
	"x-rapidapi-host": "us-real-estate-listings.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
data = response.json()

print(data)