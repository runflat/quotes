# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-20 16:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quotes',
            name='quote_participant',
            field=models.ManyToManyField(related_name='favorites', to='quotes.User'),
        ),
    ]
