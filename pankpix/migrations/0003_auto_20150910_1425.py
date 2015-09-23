# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pankpix', '0002_auto_20150910_1416'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='album',
            name='img',
        ),
        migrations.AddField(
            model_name='gallery',
            name='album',
            field=models.ForeignKey(to='pankpix.Album'),
        ),
        migrations.AddField(
            model_name='gallery',
            name='img',
            field=models.ForeignKey(to='pankpix.Image'),
        ),
    ]
