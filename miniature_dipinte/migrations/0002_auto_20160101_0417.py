# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miniature_dipinte', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='miniatura',
            name='punteggio',
            field=models.IntegerField(blank=True),
            preserve_default=True,
        ),
    ]
