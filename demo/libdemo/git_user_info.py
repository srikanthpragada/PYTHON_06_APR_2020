
import requests

URL = "https://api.github.com/users/srikanthpragada"

response = requests.get(URL)
if response.status_code == 200:  # OK
    details = response.json()    # JSON to Dict
    print("Name    : ", details['name'])
    print("Company : ", details['company'])
    print("Location: ", details['location'])
else:
    print("Sorry! User not found!")


