import datetime

from django.shortcuts import render
from django.http import HttpResponse

from django.views.decorators.cache import cache_page


@cache_page(10)
def current_time(request):
    now = datetime.datetime.now().strftime('%H:%M:%S')
    return HttpResponse('''<h1>Now is <string>%s</string></h1>''' % now)
