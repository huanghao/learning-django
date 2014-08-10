from django.shortcuts import render
from django.shortcuts import resolve_url
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages



def profile(request):
    return render(request, 'profile.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Please login with the account created")
            return HttpResponseRedirect(resolve_url('login'))
    else:
        form = UserCreationForm()
    context = {'form': form}
    return TemplateResponse(request, 'signup.html', context)
