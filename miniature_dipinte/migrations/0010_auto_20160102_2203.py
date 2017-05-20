# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miniature_dipinte', '0009_auto_20160101_2224'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='classe_modello',
            options={'ordering': ['tipo'], 'verbose_name': 'Classe Modello', 'verbose_name_plural': 'Classi Modello'},
        ),
        migrations.AlterModelOptions(
            name='miniatura',
            options={'ordering': ['-stato', 'fine', 'inizio'], 'verbose_name_plural': 'Miniature'},
        ),
        migrations.AlterField(
            model_name='miniatura',
            name='tipo',
            field=models.CharField(blank=True, max_length=6, null=True, choices=[(b'whft', b'WHF Truppa'), (b'whfe', b'WHF Elite'), (b'wh40kt', b'WH40k Truppa'), (b'wh40ke', b'WH40k Elite'), (b'df', b'Dread Fleet'), (b'fsy', b'Fantasy'), (b'stco', b'Storico'), (b'ww2', b'WWII'), (b'mno', b'Moderno'), (b'scfy', b'Scify')]),
            preserve_default=True,
        ),
    ]
