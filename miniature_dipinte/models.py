from django.db import models


class Classe_Modello(models.Model):
    tipo = models.CharField(max_length=50)
    durata = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return '%s' % self.tipo

    class Meta:
        ordering = ['tipo']
        verbose_name = "Classe Modello"
        verbose_name_plural = "Classi Modello"


class Esercito(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return '%s' % self.nome

    class Meta:
        ordering = ['nome']
        verbose_name = "Esercito/Marca"
        verbose_name_plural = "Eserciti/Marche" 


class Miniatura(models.Model):
    stati = (('DI', 'Da Iniziare'),
             ('IC', 'In Corso'),
             ('FI', 'Finito')
             )
    tipi = (('whft', 'WHF Truppa'),
            ('whfe', 'WHF Elite'),
            ('wh40kt', 'WH40k Truppa'),
            ('wh40ke', 'WH40k Elite'),
            ('scc', 'Scenici'),
            ('df', 'Dread Fleet'),
            ('bb', 'Blood Bowl'),
            ('fsy', 'Fantasy'),
            ('stco', 'Storico'),
            ('ww2', 'WWII'),
            ('mno', 'Moderno'),
            ('scfy', 'Scify'),
            )
    stato = models.CharField(max_length=2, choices=stati, default='DI',
                             null=True, blank=True)
    tipo = models.CharField(max_length=6, choices=tipi, null=True, blank=True)
    punteggio = models.IntegerField(null=True, blank=True)
#    esercito = models.CharField(max_length=100, null=True, blank=True)
    esercito2 = models.ForeignKey(Esercito, null=True, blank=True,
                                  verbose_name='Esercito')
    nome = models.CharField(max_length=100)
    classe_modello = models.ForeignKey(Classe_Modello, null=True, blank=True)
    inizio = models.DateField(null=True, blank=True)
    fine = models.DateField(null=True, blank=True)
    durata = models.IntegerField(null=True, blank=True,)
    n_pezzi = models.IntegerField(null=True, blank=True)
    immagine = models.ImageField(upload_to='immagini', null=True, blank=True)
    
    def __str__(self):
        return '%s' % self.nome

    class Meta:
        verbose_name_plural = "Miniature"
        ordering = ['-stato', 'fine', 'inizio', ]
