from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'djordini.views.home', name='home'),
                       url(r'^miniature_dipinte/', include('miniature_dipinte.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       )
