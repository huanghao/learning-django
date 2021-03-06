Must-have Django plug-ins
=========================

Search on pypi
-------------

https://pypi.python.org/pypi?%3Aaction=search&term=django&submit=search


Very famous packages
--------------------

[Django OAuth Toolkit](http://django-oauth-toolkit.readthedocs.org/en/latest/)

    provides out of the box all the endpoints, data and logic needed to
    add OAuth2 provider capabilities to your Django projects. It can be
    nicely integrated with Django REST framework.

[Django Guardian](http://django-guardian.readthedocs.org/)

    implements a per object permissions for your models.

[Django Authentication Using LDAP](https://pythonhosted.org/django-auth-ldap/)

[Cripy forms](http://django-crispy-forms.readthedocs.org/en/latest/)

[Django REST framework](http://www.django-rest-framework.org/)

    Django REST framework is a powerful and flexible toolkit that
    makes it easy to build Web APIs.


[Celery](http://www.celeryproject.org/)

    Celery is an asynchronous task queue/job queue based on
    distributed message passing. It is focused on real-time
    operation, but supports scheduling as well.

[Django stored messages](http://django-stored-messages.readthedocs.org/en/latest/)

    The app integrates smoothly with Django’s messages framework
    (django.contrib.messages), but users can decide which messages
    have to be stored on the database backend and kept available
    over sessions.

[South](http://south.readthedocs.org/en/latest/about.html)

    South brings migrations to Django applications. Its main objectives
    are to provide a simple, stable and database-independent migration
    layer to prevent all the hassle schema changes over time bring to
    your Django applications.

[Debug toolbar](https://github.com/django-debug-toolbar/django-debug-toolbar)

[Django extensions](http://django-extensions.readthedocs.org/en/latest/)

[Selenium](http://www.seleniumhq.org/)

Best practices
--------------

Principle

- PEP20 -- [The Zen of Python](http://legacy.python.org/dev/peps/pep-0020/)
- DRY principle -- [Dont Repeat Yourself](http://c2.com/cgi/wiki?DontRepeatYourself)
- [Django Design philosophies](https://docs.djangoproject.com/en/dev/misc/design-philosophies/)

Code style

- PEP8  -- [Style Guide for Python Code](http://legacy.python.org/dev/peps/pep-0008/)
- [Django code style](https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/coding-style/)
- flake8

Environment

- virtualenv

    venv in py3
    virtualenvwrapper

- pip

    requirements.txt, test-requirements.txt
    pypi

- multiple settings files

    dev, testing, staging, production
    maintain them in version control system

- Configuration management

    Puppet
    Ansible/Salt

- Continue Integration

    Travis-CI
    Jenkins/Builtbot

Development

- django.contrib
- 3rd-party apps
- Unit tests
- Fat models, thin views and stupid templates !
- Code review: Gerrit, github.com

Services

- github.com
- Travis-ci: CI
- landscape.io: Keep technical debt under control
- coversall.io: Coverage
- SauceLabs.com: Testing
- getsentry.com: Monitoring

References
----------

1. [Must-have Django packages](https://devcharm.com/articles/79/must-have-django-packages/)
1. [Django packages](https://www.djangopackages.com/)
1. [33 projects that make developing django apps awesome](http://elweb.co/33-projects-that-make-developing-django-apps-awesome/)
1. [12 tips on Django Best Practices](http://www.slideshare.net/DZPM/12-tips-on-django-best-practices)
1. [Django Best Practices](http://lincolnloop.com/django-best-practices/index.html)
