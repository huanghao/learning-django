Views and URLConfs
==================

Start application
-----------------

    $ python manage.py startapp polls

    Add the new app in settings.INSTALLED_APPS

Add the first view and urlconf
------------------------------

    add hello() in views.py

    input: request
    output: response

    mapping url pattern /hello to hello() view function

Regular expression basic
------------------------

    .(dot)
    \d
    [A-Z]
    [a-z]
    [A-Za-z]
    +
    [^/]+
    ?
    *
    {1,3}

    https://docs.python.org/2/library/re.html

Page not found: 404
-------------------

    http://localhost:8000/bye

    Debug mode: settings.DEBUG

How Django processes a request
------------------------------

    - settings.ROOT_URLCONF

    - urlpatterns in format of django.conf.urls.patterns()

    - runs through each URL pattern, and stops at the first one that matches the requested URL

    - once it matches, django imports and calls the given view, with argument as follows:

        - HttpRequest instance

        - RE groups

        - optional kwargs to django.conf.urls.url()

    - if no match, or if exception occurs, django invokes an appropriate error-handing view

Second view
-----------

    add current_datetime() in views.py

    mapping /time to current_datetime()

    settings.TIME_ZONE = 'Asia/Shanghai'

URLConf and Loose Coupling
--------------------------

    url pattern <=> view name

Third view
----------

    add view one_hour_ahead()

    add url /time/plus/1

Django's pretty error pages
---------------------------

    make some errors in views

    stack trace

    environment

HttpRequest
-----------

Attributes (not complete)

    body: raw HTTP body as byte string
    path
    method
    encoding

    GET
    POST
    REQUEST: POST or GET
    COOKIES
    FILES
    META
        - CONTENT_LENGTH
        - CONTENT_TYPE
        - HTTP_HOST
        - HTTP_REFERER
        - HTTP_USER_AGENT
        - REMOTE_ADDR
        - REMOTE_HOST

    user
    session

HttpResponse
------------

__init__

    content=''
    content_type
    status=200
    reason

Methods (not complete)

    set_cookie()
    delete_cookie()
    tell()
    write()

Subclasses

    302: HttpResponseRedirect
    301: HttpResponsePermanentRedirect
    304: HttpResponseNotModified    

    400: HttpResponseBadRequest
    404: HttpResponseNotFound
    403: HttpResponseForbidden
    405: HttpResponseNotAllowed
    410: HttpResponseGone

    500: HttpResponseServerError

    StreamingHttpResponse