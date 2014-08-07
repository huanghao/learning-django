from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django import forms
from django.contrib import messages 


class ContactForm(forms.Form):

    subject = forms.CharField(max_length=100)
    message = forms.CharField()
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST) # bound to the POST data
        if form.is_valid(): # All validation rules pass
            sender = form.cleaned_data['sender']
            url = '/thanks/' + sender
            return HttpResponseRedirect(url)
    else:
        form = ContactForm() # An unbound form

    return render(request, 'form.html', {
        'form': form,
    })


def thanks(request, who):
    return HttpResponse("Thanks <em>%s</em> !" % who)

from books.models import Author, Book

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'title', 'birth_date']

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'authors']

def model_form_view(request, kclass):
    if request.method == 'POST':
        form = kclass(request.POST)
        if form.is_valid():
            obj = form.save()
            msg = "%s(%d) created" % (obj.__class__.__name__, obj.pk)
            messages.success(request, msg)
            return HttpResponseRedirect('/created')
    else:
        form = kclass()
    return render(request, 'form.html', {
        'form': form,
    })

def author(request):
    return model_form_view(request, AuthorForm)

def book(request):
    return model_form_view(request, BookForm)

def created(request):
    return render(request, 'created.html')


class CalendarWidget(forms.TextInput):
    class Media:
        css = {
            'all': ('pretty.css',)
            }
        js = ('animations.js', 'actions.js')
