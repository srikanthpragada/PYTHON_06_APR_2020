import requests

URL = "https://restcountries.eu/rest/v2/all"

response = requests.get(URL)
if response.status_code != 200:
    print('Sorry! Could not get details!')
    exit(1)

countries = response.json()

for c in sorted(countries, key=lambda v: v['population'], reverse=True)[:10]:
    print(f"{c['name']:50s}  {c['population']:10}")
