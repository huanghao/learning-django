from django.conf.urls import patterns, include, url

urlpatterns = patterns('polls.views',
    url(r'^hello/$', 'hello', name='hello'),
    url(r'^time/$', 'current_datetime', name='time'),

    url(r'^time/plus/(?P<offset>\d+)$', 'hours_ahead', name='time_plus'),

    url(r'^time/yesterday/$', 'hours_ahead', kwargs={'offset': -24}),
)
