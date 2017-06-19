from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^miniature_dipinte/', include('miniature_dipinte.urls')),
    url(r'^admin/', include(admin.site.urls)),
               ]
