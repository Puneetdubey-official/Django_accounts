# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-08-24 07:39
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_userprofile_image'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='userprofile',
            managers=[
                ('ludhiana', django.db.models.manager.Manager()),
            ],
        ),
    ]