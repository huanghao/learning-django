from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'learningdjango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^hello/$', 'polls.views.hello'),
    url(r'^time/$', 'polls.views.current_datetime'),
    url(r'^time/plus/(\d+)$', 'polls.views.hours_ahead'),
)
