# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miniature_dipinte', '0004_miniatura_classe_modello'),
    ]

    operations = [
        migrations.AlterField(
            model_name='miniatura',
            name='durata',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
