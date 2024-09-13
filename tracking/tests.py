from django.test import TestCase
import requests

# Create your tests here.
url = "http://localhost:8000/api/next-tracking-number/"

params = {
    'origin_country_id': 'SD',
    'destination_country_id': 'JP',
    'weight': '1.234',
    'customer_id': '75c647b7-2627-481f-bd4e-cbc6b93e1036',
    'customer_name': 'RedBox Logistics',
}

# Send a GET request with the parameters
response = requests.get(url, params=params)

# Print the response
print(response.json())