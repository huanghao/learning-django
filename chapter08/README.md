Advanced Templates
==================

Quick review template knowledge we already learned
--------------------------------------------------

Basic syntax

    variable
    tag
    filter

Inheritance

    {% extends %}
    {% block %}

Use render() in view function

Using the template system
-------------------------

Template system can work without the rest of Django.

Basic way

    1. Create a *Template* object with template code string

    2. Call the *render()* method of the *Template* object with
       a set of variables(the context)

Example:

    >>> from django.template import Template, Context
    >>> t = Template('My name is {{ name }}.')
    >>> c = Context({'name': 'Adrian'})
    >>> print t.render(c)
    My name is Adrian.
    >>> c = Context({'name': 'Fred'})
    >>> print t.render(c)
    My name is Fred.

Loading templates
-----------------

1. TEMPLATE_DIRS setting

2. get_template(name)

3. template.render(context)

Loader types
------------

TEMPLATE_LOADERS setting
Default:

    ('django.template.loaders.filesystem.Loader',
     'django.template.loaders.app_directories.Loader')

filesystem.Loader

    Loads templates from the filesystem, according to TEMPLATE_DIRS.

app_directories.Loader

    Loads templates from Django apps on the filesystem. For each app
    in INSTALLED_APPS, the loader looks for a *templates/* subdirectory.

eggs.Loader

    Just like app_directories above, but it loads templates from Python
    eggs rather than from the filesystem.

cached.Loader

    Cache the compiled templates to speed up rendering progress.

    TEMPLATE_LOADERS = (
        ('django.template.loaders.cached.Loader', (
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader',
        )),
        )


RequestContext and Context Processors
-------------------------------------

*django.template.RequestContext* adds a bunch of variables to
your template context by default. The *render()* shortcut
creates a *RequestContext*.

Context processor let you specify a number of variables that
get set in each context automatically - without you having to
specify the variables in each *render()* call.

Context processors take a request object as argument and return
a dict to be merged into the context.

Example:

    def ip_address_processor(request):
        return {'ip_address': request.META['REMOTE_ADDR']}

    def some_view(request):
        c = RequestContext(request, {
            'foo': 'bar',
        }, [ip_address_processor])
        return HttpResponse(t.render(c))

The global context processors: TEMPLATE_CONTEXT_PROCESSORS

    By default it is set to:

    ("django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages")

    RequestContext always uses *django.core.context_processors.csrf*.
    It's a security related context processor which hardcoded and
    can't be turned off by previous global setting.

    https://docs.djangoproject.com/en/1.6/ref/templates/api/#django-contrib-auth-context-processors-auth

auth

    user: auth.User instance (or AnonymousUser instance)
    perms: permissions the user has

debug

    when DEBUG is True and request.META['REMOTE_ADDR'] in INTERNAL_IPS

    debug: True
    sql_queries: A list of {'sql': ..., 'time': ...}

i18n

    LANGUAGES
    LANGUAGE_CODE

media

    MEDIA_URL

static

    STATIC_URL

csrf

    {% csrf_token %} template tag

request

    *request* which is the current HttpRequest object

messages

    *messages* a list of strings that been set via message framework

Custom template tags and filters
--------------------------------

Code layout

    polls/
        models.py
        templatetags/
            __init__.py
            poll_extras.py
        views.py

    {% load poll_extras %}

Custom template filters

    cut
    lower

Custom template tags

    Two-step process: compiling and rendering

    raw template text *compiles* into *nodes* (instance of django.template.Node)
    each node has a render() method.

    <p>The time is {% current_time "%Y-%m-%d %I:%M %p" %}.</p>