Forms
=====

Overview
--------

Purpose

    1. Display an HTML form with automatically generated form widgets.

    2. Check submitted data against a set of validation rules.

    3. Redisplay a form in the case of validation errors.

    4. Convert submitted form data to the relevant Python data types.


Concepts

    Form: collection of fields that knows how validate itself and display itself as HTML

    Field: one item that can do validation

    Widget: representation, eg. <input> or <textarea>

    Form Assets (the Media class): css and js requires to render a form

Form objects
------------

Form definition syntax

    ContactForm

Using a form in a view

    get: render a clean form with unbound form

    post: bound data in order to do validation

Processing the data from a form

    is_valid()

    cleaned_data

Display a form using a template

    {{ form }}

Specify widget

    comment = forms.CharField(widget=forms.Textarea)

Customize the form template

    Non-Field errors: {{ form.non_field_errors }}
    Field errors: {{ form.subject.erros }}
    Field: {{ form.subject }}

Built-in fields
---------------

    Similar with model fields

Built-in widgets
----------------

text

    TextInput
    NumberInput
    EmailInput
    URLInput
    PasswordInput
    HiddenInput
    DateInput
    DateTimeInput
    TimeInput
    TextArea

selector and checkbox

    CheckboxInput
    Select
    NullBooleanSelect
    SelectMulti
    RadioSelect
    CheckboxSelectMultiple

file upload

    FileInput
    ClearableFileInput

Model form
----------

    definition

    save()

Customizing validation
----------------------

clean_<xxfield> method

cleaned_data

raise django.forms.ValidationError

clean() method

Form assets
-----------

When this widget is rendering, stylesheet and javascript links will be automatically included.

    class CalendarWidget(forms.TextInput):
        class Media:
            css = {
                'all': ('pretty.css',)
            }
            js = ('animations.js', 'actions.js')

    >>> w = CalendarWidget()
    >>> print(w.media)
    <link href="/static/pretty.css" type="text/css" media="all" rel="stylesheet" />
    <script type="text/javascript" src="/static/animations.js"></script>
    <script type="text/javascript" src="/static/actions.js"></script>
