Sessions, User, and Registration
================================

What's session ? Why we need it ?

    HTTP is a stateless protocol

    A bridge to keep status between clients and server

Cookies
-------

    request.COOKIES[]

    response.set_cookie()

    security issues

Django's session framework
--------------------------

Enabling

    MIDDLEWARE_CLASSES

    - django.contrib.sessions.middleware.SesionMiddleware

    INSTALLED_APPS

    - django.contrib.sessions

    syncdb

Using sessions in views

    request.session["fav_color"] = "blue"

    fav_color = request.session["fav_color"]

    del request.session["fav_color"]

    if "fav_color" in request.session

Using sessions outside of views

    sessionid is stored in browser's cookies

    >>> from django.contrib.sessions.models import Session
    >>> s = Session.objects.get(pk='2b1189a188b44ad18c35e113ac6ceead')
    >>> s.expire_date
    datetime.datetime(2005, 8, 20, 13, 35, 12)

    >>> s.session_data
    'KGRwMQpTJ19hdXRoX3VzZXJfaWQnCnAyCkkxCnMuMTExY2ZjODI2Yj...'
    >>> s.get_decoded()
    {'user_id': 42}

Browser-length sessions vs. Persistent sessions

    SESSION_EXPIRE_AT_BROWSER_CLOSE: default False

    SESSION_COOKIE_AGE: default two weeks

Settings

    SESSION_COOKIE_DOMAIN: default None for a standard cookie

    SESSION_COOKIE_NAME: default "sessionid"

    SESSION_COOKIE_SECURE: False

Users and Authentication
------------------------

Sessions could be used for user log-in.

auth/auth system

    Authentication

    - verify a user is who he or she claims to be

    Authorization

    - verify if the user is authorized to perform some given operation

    Users

    Permissions

    Groups

    Messages

Enabling

    INSTALLED_APPS

    - django.contrib.auth

    MIDDLEWARE_CLASSES

    - django.contrib.auth.middleware.AuthenticationMiddleware

    - after session middleware

    request.user: current logged-in user or AnonymousUser

Working with user objects
-------------------------

request.user.is_authenticated()

Attributes

    - username
    - first_name
    - last_name
    - email
    - password: hashed
    - is_staff
    - is_active
    - is_superuser
    - last_login
    - date_joined

Methods

    - is_authenticated()
    - is_anonymous()
    - get_full_name()
    - set_password(passwd)
    - check_password(passwd)
    - get_group_permissions()
    - get_all_permissions()
    - has_perm(perm)
    - has_perms(perm_list)
    - has_model_perms(app_label)
    - get_and_delete_messages()
    - email_user(subj, msg)

Many to many fields

    - groups
    - permissions

Creating users

    >>> from django.contrib.auth.models import user
    >>> user = User.objects.create_user('john', 'lennon@thebeatles.com', 'passwd')
    >>> user.save()

Creating superusers

    User.objects.create_superuser

    manage.py createsuperuser

Logging in and out
------------------

    from django.contrib import auth

    def login_view(request):
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect("/account/loggedin/")
        else:
            return HttpResponseRedirect("/account/invalid/")

    def logout_view(request):
        auth.logout(request)
        return HttpResponseRedirect("/account/loggedout/")

Limiting access to logged-in users

    def my_view(request):
        if not request.user.is_authenticated():
            return HttpResponseForbidden()

    from django.contrib.auth.decorators import login_required

    @login_required
    def my_view(request):
        ...

    from django.contrib.auth.decorators import permission_required

    @permission_required('polls.can_vote')
    def my_view(request):
        ...

Authentication views
--------------------

Django provides several views that can handle login, logout and password management.

Django provides no default template for those views

Example:

    (r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'myapp/login.html'}),

Built-in views

    - login
    - logout
    - logout_then_login
    - password_change
    - password_change_done
    - password_reset
    - password_reset_done
    - password_reset_confirm
    - password_reset_complete

Built-in forms

    - AuthenticationForm
    - PasswordChangeForm
    - PasswordResetForm
    - SetPasswordForm
    - UserChangeForm
    - UserCreationForm

Authentication data in templates
--------------------------------

Recall

    - TEMPLATE_CONTEXT_PROCESSORS
    - RequestContext
    - django.contrib.auth.context_processors.auth

Example

    {{ user.username }}

    {{ perms.foo.can_vote }}

Managing users in the admin site
--------------------------------

Example of using built-in auth views
------------------------------------

* login
* logout
* change password
* check permission
* sign up
