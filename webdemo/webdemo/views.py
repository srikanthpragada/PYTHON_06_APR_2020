from django.http import HttpResponse
from datetime import datetime


# Function view
def hello(request):
    return HttpResponse("<h1>Hello Django!</h1>")


def greet(request):
    if 'name' in request.GET:
        name = request.GET['name']  # read parameter name
    else:
        name = "Guest"

    now = datetime.now()
    if now.hour < 12:
        msg = "Good Morning"
    elif now.hour < 17:
        msg = "Good Afternoon"
    else:
        msg = "Good Evening"

    return HttpResponse(f"<h1 style='color:blue'>{msg} {name}</h1>")
