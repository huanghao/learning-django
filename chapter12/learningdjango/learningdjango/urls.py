from django.conf.urls import patterns, include, url
from django.shortcuts import render

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


urlpatterns += patterns(
    'django.contrib.auth.views',

    url(r'^accounts/login/$', 'login', name='login'),
    url(r'^accounts/logout/$', 'logout', name='logout'),
    url(r'^accounts/profile/$', profile, name='profile'),
    url(r'^accounts/password_change/$', 'password_change', name='password_change'),
    url(r'^accounts/password_change/done/$', 'password_change_done', name="password_change_done"),
)


