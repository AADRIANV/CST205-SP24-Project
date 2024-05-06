from urllib.request import urlopen
from bs4 import BeautifulSoup
import json, requests
from pprint import pprint
import ssl

ssl.create_default_context = ssl._create_unverified_context

# my_site = 'https://www.airnow.gov/?city=Monterey&state=CA&country=USA'
my_site = 'https://montereybay.noaa.gov/sitechar/mamm.html'

site_html = urlopen(my_site)
soup = BeautifulSoup(site_html, 'lxml')

paragraphs = soup.findAll('p')

# i = 0
# for p in paragraphs:
#     print(f'({i}) {p.get_text()}\n')
#     i += 1

toothed_whales = paragraphs[9].get_text().split('\n')
# for extra white space at end of array.
toothed_whales = toothed_whales[:7]

# clean up elements.
for i in range(len(toothed_whales)):
    toothed_whales[i] = toothed_whales[i].strip('\r\t ')
    toothed_whales[i] = toothed_whales[i][3:]
print(toothed_whales)

# Ninja Animals-API
API_KEY = 'EcJuXi9rxI4XHOSxCMk3Dg==TH0LjKwp33RqLqsq'
header = {
    'X-Api-Key':API_KEY,
}
for whale in toothed_whales:
    payload = {
        'name':whale,
    }
    ANIMAL_URL = 'https://api.api-ninjas.com/v1/animals'

    try:
        response = requests.get(ANIMAL_URL, params=payload, headers=header)
        data = response.json()
        pprint(data)
    except:
        print('please try again!')