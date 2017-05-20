# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miniature_dipinte', '0011_classe_modello_durata'),
    ]

    operations = [
        migrations.CreateModel(
            name='Esercito',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['nome'],
                'verbose_name': 'Esercito/Marca',
                'verbose_name_plural': 'Eserciti/Marche',
            },
            bases=(models.Model,),
        ),
    ]
