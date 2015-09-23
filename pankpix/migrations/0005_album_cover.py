# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pankpix', '0004_auto_20150910_1431'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='cover',
            field=models.ForeignKey(blank=True, to='pankpix.Image', null=True),
        ),
    ]
