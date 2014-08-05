Models
======

Model definition
----------------

    models.py
    extends models.Model
    declare models.*Field

Activate database
-----------------

$ python manage.py syncdb

    Creating tables ...
    Creating table polls_poll
    Creating table polls_choice
    Installing custom SQL ...
    Installing indexes ...
    Installed 0 object(s) from 0 fixture(s)

$ python manage.py dbshell

    mysql> show tables like 'polls_%';
    +------------------------------------+
    | Tables_in_learningdjango (polls_%) |
    +------------------------------------+
    | polls_choice                       |
    | polls_poll                         |
    +------------------------------------+
    2 rows in set (0.00 sec)

$ python manage.py help | grep sql

    sql
    sqlall
    sqlclear
    sqlcustom
    sqldropindexes
    sqlflush
    sqlindexes
    sqlinitialdata
    sqlsequencereset

$ python manage.py validate -h

$ python manage.py flush -h

$ python manage.py dumpdata -h


Play with the API
-----------------

Django shell

    $ python manage.py shell
    >>> from polls.models import Poll, Choice

Bypassing manage.py

    Set DJANGO_SETTINGS_MODULE env to "learningdjango.settings"

Basic accessing

    >>> Poll.objects.all()
    []

    >>> from polls.models import *
    >>> p = Poll(question="What's new ?")
    >>> p.save()
    >>> p.id
    1L
    >>> p.question
    "What's new ?"
    >>> p.pub_date
    datetime.datetime(2014, 8, 5, 5, 1, 44, 902538, tzinfo=<UTC>)

    >>> p.question = "What's up ?"
    >>> p.save()
    >>> p.id
    1L
    >>> p.question
    "What's up ?"
    >>> Poll.objects.all()
    [<Poll: Poll object>]

String representation

    __unicode__() method

    >>> Poll.objects.all()
    [<Poll: What's up ?>]

Selecting

    $ python manage.py flush

    $ python manage.py loaddata fixture.json

    all()
    get()
    filter()

    order_by()

    slicing[:]

Updating

    get()
    save()

    filter().update()

Deleting

    get()
    delete()

    filter().delete()

    all().delete()