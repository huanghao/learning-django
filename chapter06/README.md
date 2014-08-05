Admin site
==========

Admin site is activated by default
----------------------------------

How to

    urls.py
    INSTALLED_APPS
    MIDDLEWARE_CLASSES

Login

    Create user while syncdb

    $ python manage.py createsuperuser

    $ python manage.py runserver

    Access http://localhost:8000/admin/

    Models in django.contrib.auth

Register models
---------------

    admin.py

    admin.site.register

Basic usage
-----------

    Create, Read, Update, Delete (CRUD)

Customize the admin form
------------------------

admin.ModelAdmin

fields

fieldsets

Adding related objects
----------------------

inlines

    admin.StackedInline

    + Add another Choice
    X
    Delete

    admin.TabularInline

Customize the admin change list
-------------------------------

list_display

list_filter

search_fields

More options
------------

    https://docs.djangoproject.com/en/1.6/ref/contrib/admin/#modeladmin-options

https://docs.djangoproject.com/en/1.6/ref/contrib/admin/#inlinemodeladmin-options

Customize the admin look and feel
---------------------------------

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

mkdir -p templates/admin

copy admin/base_site.html

edit