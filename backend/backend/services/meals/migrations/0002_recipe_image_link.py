# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-14 23:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='image_link',
            field=models.URLField(blank=True),
        ),
    ]