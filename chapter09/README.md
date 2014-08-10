Advanced Models
===============

Quick review
------------

Model definition syntax

Fields

  options
  types

manage.py db related sub-commands

  syncdb
  flush
  sql
  loaddata

Model basic API

  all, filter, get
  create, save, update
  delete

Related objects
---------------

Foreign key: one to many

    One side: Choice.poll

    Other side: Poll.choice_set (RelatedManager)

    RelatedManager

        all/filter/create/delete/update

    options

    - related_name: backwards relation name

    - to_field: default to primary key

    - on_delete:

        CASCADE, PROTECT, SET_NULL, SET_DEFAULT, SET(), DO_NOTHING

        def get_sentinel_user():
            return User.objects.get_or_create(username='deleted')[0]

        class MyModel(models.Model):
            user = models.ForeignKey(User, on_delete=models.SET(get_sentinel_user))

Many to many

    One side: Book.authors

    Other side: Author.book_set (RelatedManager)

    options:

    - related_name

    - symmetrical

    Only used in the definition of ManyToManyFields on self.

    class Person(models.Model):
        friends = models.ManyToManyField("self")

    - through

        intermediary table

One to one:

    Similar to a ForeignKey with unique = True

    class MySpecialUser(models.Model):
        user = models.OneToOneField(User)
        supervisor = models.OneToOneField(User, related_name='supervisor_of')

    user.myspecialuser
    user.supervisor_of

    - related_name: the lower-case name of the current model as default value

Extra method of RelatedManager

    - add(obj1[, obj2, ...])

    p = Poll.get(pk=12)
    c = Choice.get(pk=13)
    p.choice_set.add(c)

    - create(**kwargs)

    p = Poll.get(pk=12)
    c = p.choice_set.create(choice_text=xx, votes=0)
    
    field which defines the relationship can be omitted

    - remove(obj1[, obj2, ...])

    for foreign key objects, this method only exists if null = True
    removing c from p.choice_set if equivalent to set c.poll to None,
    which is invalid if poll field doesn't have null = True.

    - clear()

    remove all

Retrieving related objects
--------------------------

select_related()

    c = Choice.objects.get(id=5)
    c.poll

    1: select from choice where id = 5
    2: select from poll where id = c.poll_id

    c = Choice.objects.select_related().get(id=5)

    select from choice c, poll p where id=5 and c.poll_id = p.id

    limited to ForeignKey and OneToOne fields

prefetch_related()

    select_related use sql join. However prefecth_related does a
    separate lookup for each relationship, and does the "joining"
    in python. It can be used for many to many relationship.

    Book.objects.all().prefetch_related('authors')

    It only need two queries:

    select from book
    select from author
    join in python side

Meta options
------------

Model inheritance
-----------------

Three styles of inheritance

    - ABC
    parent holds common info and never be used in isolation

    - Multi-table inheritance
    inherit from an existing model, and want each models have its own database table
    
    - Proxy models
    modify python-level behavior of a model, without changing models fields in any way

Abstract base classes

    There isn't table for CommonInfo. It can't be instantiated or saved
    directly. All fields from base model are stored in children tables.

    mysql> desc inherit_student;
    +------------+------------------+------+-----+---------+----------------+
    | Field      | Type             | Null | Key | Default | Extra          |
    +------------+------------------+------+-----+---------+----------------+
    | id         | int(11)          | NO   | PRI | NULL    | auto_increment |
    | name       | varchar(100)     | NO   |     | NULL    |                |
    | age        | int(10) unsigned | NO   |     | NULL    |                |
    | home_group | varchar(5)       | NO   |     | NULL    |                |
    +------------+------------------+------+-----+---------+----------------+

    mysql> desc inherit_employee;
    +---------+------------------+------+-----+---------+----------------+
    | Field   | Type             | Null | Key | Default | Extra          |
    +---------+------------------+------+-----+---------+----------------+
    | id      | int(11)          | NO   | PRI | NULL    | auto_increment |
    | name    | varchar(100)     | NO   |     | NULL    |                |
    | age     | int(10) unsigned | NO   |     | NULL    |                |
    | company | varchar(16)      | NO   |     | NULL    |                |
    +---------+------------------+------+-----+---------+----------------+

Multi-table inheritance

    Separate database tables both for base and children.

    Both models can be used normally.

    The inheritance relationship introduces links between the child and
    each of its parents (via an automatically-created OneToOneField).

    mysql> desc inherit_place;
    +---------+-------------+------+-----+---------+----------------+
    | Field   | Type        | Null | Key | Default | Extra          |
    +---------+-------------+------+-----+---------+----------------+
    | id      | int(11)     | NO   | PRI | NULL    | auto_increment |
    | name    | varchar(50) | NO   |     | NULL    |                |
    | address | varchar(80) | NO   |     | NULL    |                |
    +---------+-------------+------+-----+---------+----------------+

    mysql> desc inherit_restaurant;
    +-----------------+------------+------+-----+---------+-------+
    | Field           | Type       | Null | Key | Default | Extra |
    +-----------------+------------+------+-----+---------+-------+
    | place_ptr_id    | int(11)    | NO   | PRI | NULL    |       |
    | serves_hot_dogs | tinyint(1) | NO   |     | NULL    |       |
    | serves_pizza    | tinyint(1) | NO   |     | NULL    |       |
    +-----------------+------------+------+-----+---------+-------+

    mysql> desc inherit_office;
    +-------------------+------------+------+-----+---------+----------------+
    | Field             | Type       | Null | Key | Default | Extra          |
    +-------------------+------------+------+-----+---------+----------------+
    | place_ptr_id      | int(11)    | NO   | PRI | NULL    |       |
    | has_meeting_rooms | tinyint(1) | NO   |     | NULL    |                |
    +-------------------+------------+------+-----+---------+----------------+

    >>> Place(name='Home', address='001').save()
    >>> Restaurant(name="Cafe", address="002", serves_hot_dogs=False, serves_pizza=True).save()
    >>> Office(name="GTC", address="003", has_meeting_rooms=True).save()

    >>> Place.objects.all()
    [<Place: Home>, <Place: Cafe>, <Place: GTC>]
    >>> Place.objects.all()[1].restaurant
    <Restaurant: Cafe:Restaurant>
    >>> Place.objects.all()[2].office
    <Office: GTC:Office>

Proxy models

    Sometime, you don't need a new table for child model and only want
    to change the Python behavior of a model - perhaps to change the
    default manager, or add a new method.

    It's useful if you want to change the behavior of models defined
    by some library whose code you can change.

    >>> MyUser.objects.all()
    [<MyUser: admin>]
    >>> MyUser.objects.all()[0].full_name
    u'Hao, Huang'

Migration
---------

South

    http://south.readthedocs.org/en/latest/index.html

    It will be included in Django 1.7

    pip install South

    add 'south' in INSTALLED_APPS

    $ python manage.py help
    [south]
        convert_to_south
        datamigration
        graphmigrations
        migrate
        migrationcheck
        schemamigration
        startmigration
        syncdb
        test
        testserver

Schema migration

    class Knight(models.Model):
        name = models.CharField(max_length=100)
        of_the_round_table = models.BooleanField()

    $ ./manage.py schemamigration knight --initial
    Creating migrations directory at '.../learningdjango/knight/migrations'...
    Creating __init__.py in '.../learningdjango/knight/migrations'...
     + Added model knight.Knight
    Created 0001_initial.py. You can now apply this migration with: ./manage.py migrate knight

    $ ./manage.py migrate knight
    Running migrations for knight:
     - Migrating forwards to 0001_initial.
     > knight:0001_initial
     - Loading initial data for knight.
    Installed 0 object(s) from 0 fixture(s)


    class Knight(models.Model):
        name = models.CharField(max_length=100)
        of_the_round_table = models.BooleanField()
        dances_whenever_able = models.BooleanField()

    $ ./manage.py schemamigration knight --auto
     + Added field dances_whenever_able on knight.Knight
    Created 0002_auto__add_field_knight_dances_whenever_able.py. You can now apply this migration with: ./manage.py migrate knight


    $ ./manage.py migrate --list
     knight
      (*) 0001_initial
      ( ) 0002_auto__add_field_knight_dances_whenever_able

    $ ./manage.py migrate knight
    Running migrations for knight:
     - Migrating forwards to 0002_auto__add_field_knight_dances_whenever_able.
     > knight:0002_auto__add_field_knight_dances_whenever_able
     - Loading initial data for knight.
    Installed 0 object(s) from 0 fixture(s)

    mysql> desc knight_knight;
    +----------------------+--------------+------+-----+---------+----------------+
    | Field                | Type         | Null | Key | Default | Extra          |
    +----------------------+--------------+------+-----+---------+----------------+
    | id                   | int(11)      | NO   | PRI | NULL    | auto_increment |
    | name                 | varchar(100) | NO   |     | NULL    |                |
    | of_the_round_table   | tinyint(1)   | NO   |     | NULL    |                |
    | dances_whenever_able | tinyint(1)   | NO   |     | NULL    |                |
    +----------------------+--------------+------+-----+---------+----------------+


Data migration

    $ ./manage.py datamigration knight promote
    Created 0003_promote.py.

    $ vim 0003_promote.py

    Write your forwards() and backwards() functions
