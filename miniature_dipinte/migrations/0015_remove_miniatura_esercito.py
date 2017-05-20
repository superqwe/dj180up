# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miniature_dipinte', '0014_auto_20160106_0155'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='miniatura',
            name='esercito',
        ),
    ]
