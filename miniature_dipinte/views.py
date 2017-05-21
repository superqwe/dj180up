import datetime
import itertools

from pprint import pprint as pp

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext, loader

from miniature_dipinte.models import Miniatura

import miniature_dipinte.scaletta_miniature as scaletta_miniature
from miniature_dipinte.costanti import *

FIN = 'Miniature dipinte2.csv'

# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def importa_csv(request):
    with open(FIN) as fin:
        dati = fin.readlines()

        ldati = [x.split(';')[:7] for x in dati if x.split(';')[3]]
        
        del(ldati[0])

    for completato, punti, esercito, miniatura, inizio, fine, durata in ldati:

        if completato:
            stato = 'FI'
        else:
            stato = 'DI'

        if punti:
            if ',' in punti:
                punti = int(punti.split(',')[1])
            else:
                punti = int(punti)
        else:
            punti = None

        inizio = datetime.datetime.strptime(inizio, '%Y/%m/%d')
        fine = datetime.datetime.strptime(fine, '%Y/%m/%d')

        minia = Miniatura(stato=stato,
                          punteggio=punti,
                          esercito=esercito,
                          nome=miniatura,
                          inizio=inizio,
                          fine=fine,
                          )
        minia.save()

    return HttpResponse('scrittura efferruata')


def prossimi_dipinti(request):
    prima_miniatura = Miniatura.objects.filter(stato='DI').order_by('inizio')[0]
    ultima_miniatura = Miniatura.objects.filter(stato='DI').order_by('-inizio')[0]

    miniature = []
    for anno in range(prima_miniatura.inizio.year,
                      ultima_miniatura.fine.year+1):
        mminiature_per_anno = Miniatura.objects.filter(
            stato='DI', inizio__year=anno).order_by('inizio')

        miniature.append((anno, mminiature_per_anno))

    context = {'miniature': miniature,
               'titolo': '02 anno'}
    return render(request, 'miniature_dipinte/prossimi_dipinti.html', context)


def prossimi_dipinti_truppe(request):
    prima_miniatura = Miniatura.objects.filter(
        Q(stato='DI'),
        Q(tipo='whft') | Q(tipo='wh40kt')
        ).order_by('inizio')[0]
    ultima_miniatura = Miniatura.objects.filter(
        Q(stato='DI'),
        Q(tipo='whft') | Q(tipo='wh40kt')
        ).order_by('-inizio')[0]

    miniature = []
    for anno in range(prima_miniatura.inizio.year,
                      ultima_miniatura.fine.year+1):
        mminiature_per_anno = Miniatura.objects.filter(
            Q(stato='DI'),
            Q(tipo='whft') | Q(tipo='wh40kt'),
            Q(inizio__year=anno)).order_by('inizio')

        miniature.append((anno, mminiature_per_anno))

    context = {'miniature': miniature,
               'titolo': '03 truppe'}
    return render(request, 'miniature_dipinte/prossimi_dipinti.html', context)


def prossimi_dipinti_elite(request):
    prima_miniatura = Miniatura.objects.filter(Q(stato='DI')
                                               ).exclude(Q(tipo='whft') | Q(tipo='wh40kt')
                                                         ).order_by('inizio')[0]
    ultima_miniatura = Miniatura.objects.filter(Q(stato='DI')
                                                ).exclude(Q(tipo='whft') | Q(tipo='wh40kt')
                                                          ).order_by('-inizio')[0]

    miniature = []
    for anno in range(prima_miniatura.inizio.year,
                      ultima_miniatura.fine.year+1):
        mminiature_per_anno = Miniatura.objects.filter(
            Q(stato='DI'), Q(inizio__year=anno)
            ).exclude(Q(tipo='whft') | Q(tipo='wh40kt')
                      ).order_by('inizio')

        miniature.append((anno, mminiature_per_anno))

    context = {'miniature': miniature,
               'titolo': '04 elite'}
    return render(request, 'miniature_dipinte/prossimi_dipinti.html', context)


def dipinte(request):
    miniature = Miniatura.objects.filter(stato='FI').order_by('fine')
    context = {'miniature': miniature, }
    return render(request, 'miniature_dipinte/dipinte.html', context)


def prossimi_dipinti_generale(request):
    tipi = (('whft', L1, OFFSET_WHF_TRUPPE, False),
            ('wh40kt', L2, OFFSET_WH40K_TRUPPE, False),
            ('whfe', L1, OFFSET_WHF_ELITE, False),
            ('wh40ke', L2, OFFSET_WH40K_ELITE, False),
            ('scc', L4, OFFSET_Scenici, True),
            ('bg', L4, OFFSET_Board_Game, True),
            ('bb', L4, OFFSET_Blood_Bowl, True),
            ('fsy', L4, OFFSET_Fantasy, True),
            ('stco', L4, OFFSET_Storico, True),
            ('ww2', L4, OFFSET_WWII, True),
            ('mno', L4, OFFSET_Moderno, True),
            ('scfy', L4, OFFSET_Scify, True))
    lminia = scaletta_miniature.prossimi_dipinti_generale(tipi)

    miniature = [lminia[1], lminia[0]] if OFFSET_TRUPPE else [lminia[0],
                                                              lminia[1]]
    miniature.extend(lminia[2+OFFSET_ELITE:])
    miniature.extend(lminia[2:2+OFFSET_ELITE])

    context = {'miniature': miniature,
               'titolo': '01 generale'}
    return render(request, 'miniature_dipinte/prossimi_dipinti_generale.html',
                  context)


def marche(request):
    whf = []
    for esercito in L1:
        miniature = Miniatura.objects.filter(
            Q(stato='DI', esercito2__nome=esercito)).order_by('inizio')

        whf.append((esercito, miniature.all()))
        
    wh40k = []
    for esercito in L2:
        miniature = Miniatura.objects.filter(
            Q(stato='DI', esercito2__nome=esercito)).order_by('inizio')

        wh40k.append((esercito, miniature.all()))

    eserciti = []
    for esercito in L4:
        miniature = Miniatura.objects.filter(
            Q(stato='DI', esercito2__nome=esercito)).order_by('inizio')

        eserciti.append((esercito, miniature.all()))

    context = {'whf': whf,
               'wh40k': wh40k,
               'eserciti': eserciti,
               'titolo': 'marche'}
    return render(request, 'miniature_dipinte/marche.html', context)
