# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miniature_dipinte', '0005_auto_20160101_0532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='miniatura',
            name='esercito',
            field=models.CharField(max_length=100, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='miniatura',
            name='n_pezzi',
            field=models.IntegerField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='miniatura',
            name='stato',
            field=models.CharField(default=b'DI', max_length=2, blank=True, choices=[(b'DI', b'Da Iniziare'), (b'IC', b'In Corso'), (b'FI', b'Finito')]),
            preserve_default=True,
        ),
    ]
