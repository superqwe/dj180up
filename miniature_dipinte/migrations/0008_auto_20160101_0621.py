# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miniature_dipinte', '0007_auto_20160101_0611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='miniatura',
            name='classe_modello',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='miniatura',
            name='esercito',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='miniatura',
            name='fine',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='miniatura',
            name='immagine',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='miniatura',
            name='inizio',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='miniatura',
            name='n_pezzi',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='miniatura',
            name='punteggio',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='miniatura',
            name='stato',
            field=models.CharField(default=b'DI', max_length=2, null=True, blank=True, choices=[(b'DI', b'Da Iniziare'), (b'IC', b'In Corso'), (b'FI', b'Finito')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='miniatura',
            name='tipo',
            field=models.CharField(blank=True, max_length=6, null=True, choices=[(b'whft', b'WHF Truppa'), (b'whfe', b'WHF Elite'), (b'wh40kt', b'WH40 Truppa'), (b'wh40ke', b'WHF Elite'), (b'df', b'Dread Fleet'), (b'fsy', b'Fantasy'), (b'stco', b'Storico'), (b'ww2', b'WWII'), (b'mno', b'Moderno'), (b'scfy', b'Scify')]),
            preserve_default=True,
        ),
    ]
