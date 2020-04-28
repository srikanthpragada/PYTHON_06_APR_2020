import requests

code = input("Enter country code :")
URL = f"https://restcountries.eu/rest/v2/alpha/{code}"
response = requests.get(URL)
if response.status_code != 200:
    print('Sorry! Could not get details about country!')
    exit(1)

country = response.json()

for (k, v) in country.items():
    print(f"{k:20}  {v}")
