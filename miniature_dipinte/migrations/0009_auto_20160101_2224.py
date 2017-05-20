# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miniature_dipinte', '0008_auto_20160101_0621'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classe_Modello',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='miniatura',
            name='classe_modello',
            field=models.ForeignKey(blank=True, to='miniature_dipinte.Classe_Modello', null=True),
            preserve_default=True,
        ),
    ]
