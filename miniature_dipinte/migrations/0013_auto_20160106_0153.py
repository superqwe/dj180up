# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miniature_dipinte', '0012_esercito'),
    ]

    operations = [
        migrations.AlterField(
            model_name='miniatura',
            name='esercito',
            field=models.ForeignKey(blank=True, to='miniature_dipinte.Esercito', null=True),
            preserve_default=True,
        ),
    ]
