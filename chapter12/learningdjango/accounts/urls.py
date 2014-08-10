from django.conf.urls import patterns, include, url


urlpatterns = patterns(
    'django.contrib.auth.views',

    url(r'^login/$', 'login', name='login'),
    url(r'^logout/$', 'logout', name='logout'),
    url(r'^password_change/$', 'password_change', name='password_change'),
    url(r'^password_change/done/$', 'password_change_done', name="password_change_done"),
)

urlpatterns += patterns(
    'accounts.views',
    url(r'^profile/$', 'profile', name='profile'),
    url(r'^signup/$', 'signup', name="signup"),
)

