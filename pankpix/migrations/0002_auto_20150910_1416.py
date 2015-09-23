# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pankpix', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='img',
        ),
        migrations.AddField(
            model_name='album',
            name='img',
            field=models.ManyToManyField(to='pankpix.Image'),
        ),
    ]
