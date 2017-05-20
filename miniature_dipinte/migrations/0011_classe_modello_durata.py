# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miniature_dipinte', '0010_auto_20160102_2203'),
    ]

    operations = [
        migrations.AddField(
            model_name='classe_modello',
            name='durata',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
