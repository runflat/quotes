# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-20 21:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0002_quotes_quote_participant'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quotes',
            name='quote_participant',
        ),
        migrations.AddField(
            model_name='quotes',
            name='quotes_liked',
            field=models.ManyToManyField(related_name='favorite', to='quotes.User'),
        ),
    ]
