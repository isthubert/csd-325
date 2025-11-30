# Isaac St Hubert Module 9.2 11/30/2025
# This program prints out the response from the astros api request in python and json format

import requests
import json

response = requests.get('http://api.open-notify.org/astros.json')

print(response.status_code)

print('\n', response.json(), '\n')

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(response.json())