# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-12 04:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mall', '0002_auto_20171212_0409'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='highcategory',
            name='code',
        ),
    ]