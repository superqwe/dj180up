# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miniature_dipinte', '0003_auto_20160101_0431'),
    ]

    operations = [
        migrations.AddField(
            model_name='miniatura',
            name='classe_modello',
            field=models.CharField(max_length=100, blank=True),
            preserve_default=True,
        ),
    ]
