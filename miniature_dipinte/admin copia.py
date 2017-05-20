import datetime
import time

from pprint import pprint as pp

from django.contrib import admin

from miniature_dipinte.models import Classe_Modello, Esercito, Miniatura

import scaletta_miniature

# Azioni
def durata_modelli_finiti(modeladmin, request, queryset):
    miniature = Miniatura.objects.filter(stato = 'FI')

    for miniatura in miniature:
        miniatura.durata = (miniatura.fine - miniatura.inizio).days 
        miniatura.save()

durata_modelli_finiti.short_description = 'Calcola la durata delle miniature terminate'


def durata_classe_modello(modeladmin, request, queryset):
    classi = Classe_Modello.objects.all()

    for classe in classi:
        # miniature finite
        miniature = Miniatura.objects.filter(classe_modello = classe,
                                             stato = 'FI').values('durata',
                                                                  'n_pezzi')

        durata = [float(x['durata'] / x['n_pezzi']) for x in miniature]
        durata = sum(durata) / len(durata) + 1
        miniatura = Classe_Modello.objects.filter(tipo=classe).update(durata=durata)

        # miniature da iniziare
        miniature = Miniatura.objects.filter(classe_modello = classe,
                                             stato = 'DI')
        for miniatura in miniature:

            try:
                miniatura.durata = durata * miniatura.n_pezzi
                miniatura.save()
            except:
                print '****ERRORE*** non aggiorna la durata delle miniatura', miniatura.nome

durata_classe_modello.short_description = 'Calcola la durata delle classi di modelli'


def durata_modelli_in_corso(modeladmin, request, queryset):
    miniature = Miniatura.objects.filter(stato = 'IC')

    for miniatura in miniature:
        miniatura.durata = (miniatura.fine - miniatura.inizio).days 
        miniatura.save()
    
durata_modelli_in_corso.short_description = 'Calcola la durata delle miniature in corso'


def allunga_durata_modello_in_corso(modeladmin, request, queryset):
    for miniatura in queryset:

        if miniatura.stato == 'IC':
            miniatura.fine += datetime.timedelta(30)
            miniatura.save()

    durata_modelli_in_corso(None, None, None)

allunga_durata_modello_in_corso.short_description = 'Aumenta di 30 giorni la durata della miniatura'


def aggiorna_date_truppe(modeladmin, request, queryset):
    elenco_truppe = scaletta_miniature.elenco_truppe()
    scaletta_miniature.aggiorna_date_truppe(elenco_truppe)

aggiorna_date_truppe.short_description = 'Aggiorna le date delle truppe'


def aggiorna_date_elite(modeladmin, request, queryset):
    elenco_elite = scaletta_miniature.elenco_elite()
    scaletta_miniature.aggiorna_date_elite(elenco_elite)

aggiorna_date_elite.short_description = "Aggiorna le date dell'elite"


def aggiorna_miniature_aggiunte(modeladmin, request, queryset):
    print 'OK\nCalcola la durata dei modelli...',
    durata_classe_modello(None, None, None)
    print 'OK\nAggiorna le date delle truppe...',
    aggiorna_date_truppe(None, None, None)
    print 'OK\nAggiorna le date delle elite...',
    aggiorna_date_elite(None, None, None)
    print 'OK\n'

aggiorna_miniature_aggiunte.short_description = 'Aggiorna le date delle miniature da iniziare'
    

# Register your models here.
class MiniaturaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'stato', 'tipo', 'punteggio', 'esercito2',
                    'classe_modello', 'inizio', 'fine', 'durata', 'n_pezzi',
                    'immagine')

    list_filter = ['stato', 'tipo', 'classe_modello', 'esercito2',]

    search_fields = ['nome']

    actions = [durata_modelli_finiti,
               durata_classe_modello,
               durata_modelli_in_corso,
               allunga_durata_modello_in_corso,
               aggiorna_date_truppe,
               aggiorna_date_elite,
               aggiorna_miniature_aggiunte,
               ]


class Classe_Modello_Admin(admin.ModelAdmin):
    list_display = ('tipo', 'durata')
    actions = [durata_classe_modello]
    
admin.site.register(Classe_Modello, Classe_Modello_Admin)
admin.site.register(Esercito)
admin.site.register(Miniatura, MiniaturaAdmin)
