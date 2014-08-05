from django.conf.urls import patterns, include, url

urlpatterns = patterns('polls.views',
    url(r'^hello/$', 'hello', name='hello'),
    url(r'^time/$', 'current_datetime', name='time'),

    url(r'^time/plus/(?P<offset>\d+)$', 'hours_ahead', name='time_plus'),

    url(r'^time/yesterday/$', 'hours_ahead', kwargs={'offset': -24}),
)




from polls import views

urlpatterns += patterns('polls.views',
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<poll_id>\d+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<poll_id>\d+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),

)
