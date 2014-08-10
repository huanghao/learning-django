import hashlib
import json

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseForbidden


def welcome(request):
    name = request.REQUEST.get('name', 'Anonymous')
    return {'detail': 'Welcome %s' % name}


# >>> hashlib.sha1('jasonsecret').hexdigest()
# '8ef1ce8cea5ff2b3ffcb76e6345b6bdaee0f2c8a'

class SignCheckMiddleware(object):

    def process_request(self, request):
        sign = request.REQUEST.get('sign')

        items = sorted(request.REQUEST.items(), key=lambda i:i[0])
        base = ''.join([v for k, v in items if k != 'sign']) + 'secret'

        sign_expected = hashlib.sha1(base).hexdigest()

        if sign != sign_expected:
            return HttpResponseForbidden("403 wrong sign key")


class JsonResponseMiddleware(object):

    def process_response(self, request, response):
        if isinstance(response, HttpResponse):
            return response

        json_string = json.dumps(response)
        return HttpResponse(json_string, content_type='application/json')
