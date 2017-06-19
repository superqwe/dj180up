# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-19 20:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('miniature_dipinte', '0016_auto_20160108_0316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='miniatura',
            name='esercito2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='miniature_dipinte.Esercito', verbose_name='Esercito'),
        ),
        migrations.AlterField(
            model_name='miniatura',
            name='immagine',
            field=models.ImageField(blank=True, null=True, upload_to='immagini'),
        ),
        migrations.AlterField(
            model_name='miniatura',
            name='stato',
            field=models.CharField(blank=True, choices=[('DI', 'Da Iniziare'), ('IC', 'In Corso'), ('FI', 'Finito')], default='DI', max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='miniatura',
            name='tipo',
            field=models.CharField(blank=True, choices=[('whft', 'WHF Truppa'), ('whfe', 'WHF Elite'), ('wh40kt', 'WH40k Truppa'), ('wh40ke', 'WH40k Elite'), ('scc', 'Scenici'), ('df', 'Dread Fleet'), ('bb', 'Blood Bowl'), ('fsy', 'Fantasy'), ('stco', 'Storico'), ('ww2', 'WWII'), ('mno', 'Moderno'), ('scfy', 'Scify'), ('bg', 'Board Game')], max_length=6, null=True),
        ),
    ]
