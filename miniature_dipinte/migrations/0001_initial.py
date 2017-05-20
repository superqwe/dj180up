# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Miniatura',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('stato', models.CharField(default=b'DI', max_length=2, choices=[(b'DI', b'Da Iniziare'), (b'IC', b'In Corso'), (b'FI', b'Finito')])),
                ('tipo', models.IntegerField()),
                ('punteggio', models.IntegerField()),
                ('esercito', models.CharField(max_length=100)),
                ('nome', models.CharField(max_length=100)),
                ('inizio', models.DateField(blank=True)),
                ('fine', models.DateField(blank=True)),
                ('durata', models.IntegerField(blank=True)),
                ('n_pezzi', models.IntegerField()),
                ('immagine', models.ImageField(upload_to=b'', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
