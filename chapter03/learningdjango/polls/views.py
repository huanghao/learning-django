import datetime

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello(request):
    return HttpResponse('Hello world')


def current_datetime(request):
    now = datetime.datetime.now()
    return HttpResponse('<html><body>It is now %s.</body></html>' % now)


def hours_ahead(request, offset):
    dt = datetime.datetime.now() + datetime.timedelta(hours=int(offset))
    return HttpResponse('<html><body>It is now %s.</body></html>' % dt)
    
