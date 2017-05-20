# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miniature_dipinte', '0013_auto_20160106_0153'),
    ]

    operations = [
        migrations.AddField(
            model_name='miniatura',
            name='esercito2',
            field=models.ForeignKey(blank=True, to='miniature_dipinte.Esercito', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='miniatura',
            name='esercito',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
    ]
