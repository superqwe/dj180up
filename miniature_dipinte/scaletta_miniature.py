import datetime
import itertools
# import time

from pprint import pprint as pp

from django.db.models import Q

from miniature_dipinte.models import Classe_Modello, Esercito, Miniatura

from miniature_dipinte.costanti import *

def elenco_truppe():
    whf = elenco_truppe2(L1, 'whft', OFFSET_WHF_TRUPPE)
    wh40k = elenco_truppe2(L2, 'wh40kt', OFFSET_WH40K_TRUPPE)
    lwh = [whf, wh40k]

    wh = itertools.cycle(range(2))

    for i, x in enumerate(wh):

        if i >= OFFSET_TRUPPE:
            break

    miniature = []
    for n in range(NUMERO_TOTALE_DI_MINIATURE):

        for i, e in enumerate(wh):

            try:
                # print(i, e, n)
                minia = lwh[e][n]
                miniature.append(minia)
            except IndexError:
                pass

            if i == 1:
                break

    # pp(miniature)
    return miniature


def elenco_truppe2(lista, tipo, offset=0):
    leserciti = []
    for esercito in lista:
        miniature = Miniatura.objects.filter(
            tipo=tipo, stato='DI', esercito2__nome=esercito).order_by(
                'punteggio', 'nome')

        leserciti.append(miniature)

    miniature = []
    neserciti = len(lista)
    esercito = itertools.cycle(range(neserciti))

    for i, x in enumerate(esercito):
        if i >= offset - 1:
                break
                
    termina_ciclo = neserciti
    for n in range(NUMERO_TOTALE_DI_MINIATURE):    
        
        for i, e in enumerate(esercito):
            # print(i, e, n, termina_ciclo)
            if termina_ciclo == 0:
                break

            try:
                minia = leserciti[e][n]
                # print(minia)
                miniature.append(minia)
                termina_ciclo = neserciti
            except IndexError:
                termina_ciclo -= 1

            if i == neserciti - 1:
                    break

    return miniature


def aggiorna_date_truppe(elenco_truppe):
    truppa_in_corso = Miniatura.objects.filter(
        Q(stato='IC'),
        Q(tipo='whft') | Q(tipo='wh40kt')).order_by('-fine')[0]

    data = truppa_in_corso.fine

    for minia in elenco_truppe:
        # print(minia.nome)
        minia.inizio = data
        data += datetime.timedelta(minia.durata)
        minia.fine = data
        minia.save()

    
def elenco_elite():
    eserciti = ('scc', 'df', 'bb',
                'fsy', 'stco', 'ww2',
                'mno', 'scfy')
    offset = (OFFSET_Scenici, OFFSET_Dread_Fleet, OFFSET_Blood_Bowl,
              OFFSET_Fantasy, OFFSET_Storico, OFFSET_WWII,
              OFFSET_Moderno, OFFSET_Scify)
    
    whf = elenco_truppe2(L1, 'whfe', OFFSET_WHF_ELITE)
    wh40k = elenco_truppe2(L2, 'wh40ke', OFFSET_WH40K_ELITE)

    leserciti = [whf, wh40k]

    for esercito, offset in zip(eserciti, offset):
        elenco = elenco_truppe2(L4, esercito, offset)
        leserciti.append(elenco)
  
    neserciti = len(leserciti)

    esercito = itertools.cycle(range(neserciti))

    for i, x in enumerate(esercito):
        if i >= OFFSET_ELITE - 1:
            break

    miniature = []
    for n in range(NUMERO_TOTALE_DI_MINIATURE):

        for i, e in enumerate(esercito):
            if i >= neserciti - 1:
                break
        
            try:
                minia = leserciti[e][n]
                miniature.append(minia)
            except IndexError:
                pass

    return miniature


def aggiorna_date_elite(elenco_elite):
    elite_in_corso = Miniatura.objects.filter(
        Q(stato='IC')).exclude(
            Q(tipo='whft') | Q(tipo='wh4okt')).order_by('-fine')[0]

    data = elite_in_corso.fine
   
    for minia in elenco_elite:
        minia.inizio = data
        data += datetime.timedelta(minia.durata)
        minia.fine = data
        minia.save()

        
def prossimi_dipinti_generale(tipi):
    miniature = []
    for tipo, lista_esercito, offset, salta in tipi:

        neserciti = len(lista_esercito)
        iesercito = itertools.cycle(lista_esercito)

        for i, x in enumerate(iesercito):
            if i >= offset - 1:
                break
            
        lminia = []
        for i, esercito in enumerate(iesercito):

            try:
                miniatura = Miniatura.objects.filter(
                    stato='DI', tipo=tipo, esercito2__nome=esercito
                    ).order_by('inizio')[0]
                lminia.append(miniatura)
            except IndexError:

                if not salta:
                    miniatura = {'esercito2': esercito, 'tipo': tipo}
                    lminia.append(miniatura)

            if i == neserciti - 1:
                break

        miniature.append(lminia)
        
    return miniature
