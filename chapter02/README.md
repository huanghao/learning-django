Start project
-------------

    $ django-admin.py startproject learningdjango

Run server
----------

    $ python manage.py runserver
    Starting development server at http://127.0.0.1:8000/

    $ python manage.py runserver 0.0.0.0:8000

Open a page
-----------

    Open http://localhost:8000 in browser

Setup Database
--------------

    Database configuration

    $ mysql -uroot -e 'create database learningdjango default character set utf8'

    $ python manage.py syncdb

    $ python manage.py dbshell

Manage.py
---------

    $ python manage.py shell

    $ python manage.py help
