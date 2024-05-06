import json, requests
from pprint import pprint
from ebird.api import get_observations, get_regions

# Ninja Animals-API
API_KEY = 'EcJuXi9rxI4XHOSxCMk3Dg==TH0LjKwp33RqLqsq'
header = {
    'X-Api-Key':API_KEY,
}
payload = {
    'name':'Sperm Whale',
}
ANIMAL_URL = 'https://api.api-ninjas.com/v1/animals'

try:
    response = requests.get(ANIMAL_URL, params=payload, headers=header)
    data = response.json()
    pprint(data)
except:
    print('please try again!')

# eBird API
# County Code: US-CA-053
API_KEY = 'j9q2bq6fa71e'
# observations = get_observations(API_KEY, 'US-CA-053', back=7)
# pprint(observations)