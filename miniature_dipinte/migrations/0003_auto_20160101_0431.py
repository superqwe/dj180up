# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miniature_dipinte', '0002_auto_20160101_0417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='miniatura',
            name='tipo',
            field=models.CharField(max_length=6, choices=[(b'whft', b'WHF Truppa'), (b'whfe', b'WHF Elite'), (b'wh40kt', b'WH40 Truppa'), (b'wh40ke', b'WHF Elite'), (b'df', b'Dread Fleet'), (b'fsy', b'Fantasy'), (b'stco', b'Storico'), (b'ww2', b'WWII'), (b'mno', b'Moderno'), (b'scfy', b'Scify')]),
            preserve_default=True,
        ),
    ]
