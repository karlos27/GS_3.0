# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-30 14:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuaris', '0004_remove_perfil_alta'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='perfil',
            options={'ordering': ['correu'], 'verbose_name_plural': 'Profile'},
        ),
    ]
