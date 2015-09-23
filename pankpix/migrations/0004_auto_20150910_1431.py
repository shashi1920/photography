# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pankpix', '0003_auto_20150910_1425'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='date_added',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='gallery',
            name='date_added',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='image',
            name='date_added',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='permission',
            name='date_added',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
