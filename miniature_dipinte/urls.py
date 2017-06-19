from django.conf.urls import url

from miniature_dipinte import views

urlpatterns = [url(r'^prossimi_dipinti$',
                   views.prossimi_dipinti,
                   name='prossimi_dipinti'),
               url(r'^prossimi_dipinti_generale$',
                   views.prossimi_dipinti_generale,
                   name='prossimi_dipinti_generale'),
               url(r'^prossimi_dipinti_truppe$',
                   views.prossimi_dipinti_truppe,
                   name='prossimi_dipinti_truppe'),
               url(r'^prossimi_dipinti_elite$',
                   views.prossimi_dipinti_elite,
                   name='prossimi_dipinti_elite'),
               url(r'^dipinte$',
                   views.dipinte,
                   name='dipinte'),
               url(r'^marche$',
                   views.marche,
                   name='marche'),
               # url(r'^importa_csv/$',
               #    views.importa_csv,
               #    name='importa_csv'),
               ]
