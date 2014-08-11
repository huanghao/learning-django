Deploying Django
================

Using different settings for production
---------------------------------------

Independent settings files

    settings_production.py

    DJANGO_SETTINGS_MODULE points to

"Base" for development + second for production

    /etc/settings_production.py

    import
    exec_file

Checklist
---------

Critical settings

    SECRET_KEY

    DEBUG & TEMPLATE_DEBUG

Environment-specific settings

    ALLOWED_HOSTS

        Request.Host
        ['*']
        ['.intel.com']

    CACHES

    DATABASES

    EMAIL_BACKEND

    STATIC_ROOT & STATIC_URL

        - css & js

    MEDIA_ROOT & MEDIA_URL

HTTPS

    CSRF_COOKIE_SECURE

    SESSION_COOKIE_SECURE

Error reporting

    LOGGING

    ADMINS & MANAGERS

        - server error

        - broken link with referer

Customize the default error views

    In your templates root directory

    404.html (page not found)
    500.html (server error)
    403.html (HTTP forbidden)
    400.html (bad request)


WSGI + Apache
-------------

    install and enable mod_wsgi

    apache.conf

    $ python manage.py collectstatic

Ansible
-------

Ansible technology

* YAML syntax

* Jinja2 templates

* SSH

* Ansible module library

* Django manage.py commands module

An example

    https://github.com/jcalazan/ansible-django-stack

    Google "ansible django" for more resource
