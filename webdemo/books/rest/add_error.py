import requests

data = {'title': "Error Book"}

resp = requests.post("http://localhost:8000/books/rest/books/", data)
if resp.status_code == 200:
    book = resp.json()
    print("Book added successfully with book id : ", book['id'])
else:
    errors = resp.json()
    print("Errors :", errors)
    print("Sorry! Could not add book!")
