# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-03 09:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuaris', '0014_auto_20170802_1843'),
    ]

    operations = [
        migrations.RenameField(
            model_name='arxius',
            old_name='nom_usuari',
            new_name='usuari',
        ),
    ]
