# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-02 16:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuaris', '0013_auto_20170714_1252'),
    ]

    operations = [
        migrations.RenameField(
            model_name='arxius',
            old_name='usuari',
            new_name='nom_usuari',
        ),
    ]
