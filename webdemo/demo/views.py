from django.shortcuts import render
import sqlite3
from django.http import HttpResponse
import random


def home(request):
    return render(request,  # request object
                  'summary.html',  # Template
                  {
                      'title': 'Django Application',
                      'topics': ['Templates', 'Forms', 'ORM', 'AJAX', 'REST']
                  }  # Context
                  )


def interest_calculation(request):
    if 'amount' in request.POST:  # data is present, so process it
        amount = float(request.POST['amount'])
        rate = float(request.POST['rate'])
        interest = amount * rate / 100
        return render(request, 'interest.html',
                      {'amount': amount, 'rate': rate, 'interest': interest})
    else:
        return render(request, 'interest.html')


def ajax_demo(request):
    return render(request, 'ajax_demo.html')


def message(request):
    messages = ['Winners never quit, quitters never win',
               'If you are not failing, you are not growing',
               'Be the change that you wish to see in the world',
               'I will prepare and some day my chance will come'
               ]
    msg = messages[random.randint(0,3)]
    return HttpResponse(msg)
