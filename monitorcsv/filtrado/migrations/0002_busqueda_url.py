# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-20 20:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filtrado', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='busqueda',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
