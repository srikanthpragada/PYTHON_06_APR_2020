from django.shortcuts import render
import sqlite3
from django.http import HttpResponse



def home(request):
    return render(request,  # request object
                  'home.html',  # Template
                  {
                      'title': 'Django Application',
                      'topics': ['Templates', 'Forms', 'ORM', 'AJAX', 'REST']
                  }  # Context
                  )


def interest_calculation(request):
    if 'amount' in request.GET:  # data is present, so process it
        amount = float(request.GET['amount'])
        rate = float(request.GET['rate'])
        interest = amount * rate / 100
        return render(request, 'interest.html',
                      {'amount': amount, 'rate': rate, 'interest': interest})
    else:
        return render(request, 'interest.html')
