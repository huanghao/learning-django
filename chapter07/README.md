Advanced Views and URLConfs
===========================

Quick review
------------

    urls.py
    mapping url pattern to view function


Improved urls.py
----------------

include polls.urls

common prefix "polls.views"

Visit http://localhost:8000/polls/hello

url() arguments
---------------

regex

    Named groups
    (?P<name>...)
    https://docs.python.org/2/library/re.html#regular-expression-syntax

    Keyword Arguments vs. Positional Arguments

view

    function
    string

kwargs

    can be passed in a dict to the target view

name

    Use in view function
    
    >>> from django.core.urlresolvers import reverse
    >>> reverse('hello')
    '/polls/hello/'
    >>> reverse('time_plus', args=(2,))
    '/polls/time/plus/2'

    https://docs.djangoproject.com/en/1.6/ref/urlresolvers/#module-django.core.urlresolvers

    Use in template

    {% url 'time_plus' 2 %}

    https://docs.djangoproject.com/en/1.6/ref/templates/builtins/#url


Write views that actually do something
--------------------------------------

index()

Template namespacing

    BASE_DIR/polls/templates/polls/index.html

    RequestContext vs Context
    user, csrf ...
    TEMPLATE_CONTEXT_PROCESSORS
    https://docs.djangoproject.com/en/dev/ref/templates/api/#subclassing-context-requestcontext

    A shortcut: render()

detail()

    Raise Http404 error

    A shortcut: get_object_or_404()

Removing hardcoded URLs in templates

    {% url 'detail' poll.pk %}

Namespacing URL names

    url(r'^polls/', include('polls.urls', namespace="polls")),

    {% url 'polls:detail' poll.id %}