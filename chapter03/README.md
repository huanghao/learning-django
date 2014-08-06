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

HttpResponse
------------