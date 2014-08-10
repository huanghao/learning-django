from django.conf.urls import patterns, include, url
from django.shortcuts import render
from django.shortcuts import resolve_url
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'learningdjango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)


def profile(request):
    return render(request, 'profile.html')

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

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


urlpatterns += patterns(
    'django.contrib.auth.views',

    url(r'^accounts/login/$', 'login', name='login'),
    url(r'^accounts/logout/$', 'logout', name='logout'),
    url(r'^accounts/profile/$', profile, name='profile'),
    url(r'^accounts/password_change/$',
        'password_change', name='password_change'),
    url(r'^accounts/password_change/done/$',
        'password_change_done', name="password_change_done"),
    url(r'accounts/signup', signup, name="signup"),
)
