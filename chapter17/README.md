Testing
=======

Automated testing is an extremely useful bug-killing tool for the
modern Web developer.

Unit test
---------

Std lib unittest

py.test

nose

coverage

pylint/flake8

Django test
-----------

$ python manage.py test

Test databases

    test_ + <your database name in settings.py>

TestClient

    >>> from django.test.client import Client
    >>> c = Client()
    >>> response = c.post('/login/', {'username': 'john', 'password': 'smith'})
    >>> response.status_code
    200
    >>> response = c.get('/customer/details/')
    >>> response.content
    '<!DOCTYPE html...'

TestCase

    - Automatic loading of fixtures.
    - Wraps each test in a transaction.
    - Creates a TestClient instance.
    - Django-specific assertions for testing for things like redirection
      and form errors.

LiveServerTestCase

    It launches a live Django server in the background on setup, and shuts
    it down on teardown.

    This allows the use of automated test clients other than the Django
    dummy client such as, for example, the Selenium client, to execute a
    series of functional tests inside a browser and simulate a real user’s
    actions.

    xvfb: Headless X server
    phantomjs.org: Headless WebKit with Javascript API
