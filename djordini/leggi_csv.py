from pprint import pprint as pp

FIN = 'Miniature dipinte2.csv'

def leggi():
    with open(FIN) as fin:
        dati = fin.readlines()

        ldati = [x.split(';')[:7] for x in dati if x.split(';')[3]]
        
        del(ldati[0])

    return ldati

if __name__ == '__main__':
    leggi()
