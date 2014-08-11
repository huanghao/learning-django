Templates
=========

Using template in hours_ahead() view
------------------------------------

    mkdir templates/

    Django searches templates/ sub-directory in each of INSTALLED_APPS

    settings.TEMPLATE_DIRS

    render()

Template basic syntax
---------------------

Variables

    {{ variable }}

    {{ var.attr }}
    Dictionary look up
    Attribute look up
    Method call
    List-index look up

    settings.TEMPLATE_STRING_IF_INVALID
    '' by default

Tags

    {% tag %} content {% endtag %}

    {% if %}
    {% for %} forloop.first
    {% comment %}

    {% now %}
    {% csrf_token %}
    {% url %}
    {% with %}
    {% templatetag %}
    {% autoescape off/on %} Automatic HTML escaping

    Inheritance    
    {% extends %}
    {% block %}

    Reuse
    {% include %}
    {% load %} 

    Others: https://docs.djangoproject.com/en/1.6/ref/templates/builtins/#ref-templates-builtins-tags

Filter

    {{ variable | filter:args | filter2:args }}

    default
    length
    striptags
    safe

    Others: https://docs.djangoproject.com/en/1.6/ref/templates/builtins/#ref-templates-builtins-filters

Humanization

    https://docs.djangoproject.com/en/1.6/ref/contrib/humanize/

    INSTALLED_APP += django.contrib.humanize

    {% load humanize %}

    Filters:
    * apnumber
    * intcomma
    * naturalday
    * natrualtime
    * ordinal

Inheritance
-----------

add base.html

    block title
    block body
    css/js of jquery & bootstrap

add hello.html

    extends base.html
    block

update hello() view
