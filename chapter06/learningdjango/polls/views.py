import datetime

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello(request):
    return render(request, "hello.html")


def current_datetime(request):
    now = datetime.datetime.now()
    return HttpResponse('<html><body>It is now %s.</body></html>' % now)


def hours_ahead(request, offset):
    offset = int(offset)
    now = datetime.datetime.now() 
    dt = now + datetime.timedelta(hours=offset)
    return render(request, "datetime.html", {
            'now': now,
            'offset': offset,
            'dt': dt,
            })
