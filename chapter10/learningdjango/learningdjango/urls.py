from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'learningdjango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('books.views',
    url(r'^contact$', 'contact'),
    url(r'^thanks/(.*)$', 'thanks'),
    url(r'^author/$', 'author'),
    url(r'^book/$', 'book'),
    url(r'^created/$', 'created'),
)
