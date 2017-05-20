# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miniature_dipinte', '0015_remove_miniatura_esercito'),
    ]

    operations = [
        migrations.AlterField(
            model_name='miniatura',
            name='esercito2',
            field=models.ForeignKey(verbose_name=b'Esercito', blank=True, to='miniature_dipinte.Esercito', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='miniatura',
            name='immagine',
            field=models.ImageField(null=True, upload_to=b'immagini', blank=True),
            preserve_default=True,
        ),
    ]
