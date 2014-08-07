Models
======

Model definition
----------------

    models.py
    extends models.Model
    declare models.*Field
    automatic primary key fields

    https://docs.djangoproject.com/en/1.6/ref/models/fields/

Field options

    primay_key
    db_index
    unique

    default

    null (Default False)
    blank (Default False)

    blank is different than null. null is purely database-related,
    whereas blank is validation-related.

    If a field has blank=True, form validation will allow entry of
    an empty value. If a field has blank=False, the field will be required.

Field types

    Auto: automatically be added to your model

    Boolean
    NullBoolean

    Integer
    BigInteger
    PositiveInteger
    PositiveSmallInteger
    SmallInteger
    CommaSeparatedInteger

    Float
    Decimal

    Binary
    Char
    Text

    Date
    DateTime
    Time

    Email
    URL
    File
    FilePath
    Image
    IPAddress
    GenericIPAddress

    ForeignKey
    ManyToMany
    OneToOne

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

Creating

    >>> p = Poll.objects.create(question="What's wrong ?", pub_date="2012-12-12T01:02:03Z")
    >>> p.choice_set.create(choice_text='Not much', votes=0)
    <Choice: Not much>
    >>> p.choice_set.create(choice_text='The sky', votes=0)
    <Choice: The sky>
    >>> c = p.choice_set.create(choice_text='Just hacking again', votes=1)

    >>> c.poll
    <Poll: Poll object>
    >>> p.choice_set.all()
    [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]
    >>> p.choice_set.count()
    3

Reset data

    $ python manage.py flush

    $ python manage.py loaddata fixture.json
    Installed 5 object(s) from 1 fixture(s)

Selecting

    >>> Poll.objects.get(pk=2).choice_set.all()
    [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]

    >>> Poll.objects.get(pk=3)
    Traceback (most recent call last):
      File "<console>", line 1, in <module>
    DoesNotExist: Poll matching query does not exist.

    >>> Choice.objects.filter(choice_text__startswith='Just')
    [<Choice: Just hacking again>]

    >>> Poll.objects.get(pk=2).choice_set.filter(votes=0).order_by('-choice_text')
    [<Choice: The sky>, <Choice: Not much>]

    >>> Poll.objects.get(pk=2).choice_set.filter(votes=0)[1:]
    [<Choice: The sky>]

Updating

    Single
    o = get()
    o.attr = value
    o.save()

    Multiple
    >>> Choice.objects.filter(poll__pk=2).update(poll=1)
    3L
    >>> Choice.objects.filter(poll__pk=2)
    []
    >>> Choice.objects.filter(poll__pk=1)
    [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]

Deleting

    Single
    o = get()
    o.delete()

    Multiple
    filter().delete()

    All
    all().delete()

Manager
-------

Aggregation
-----------

Multiple databases
------------------
