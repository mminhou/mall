# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-12 05:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mall', '0007_auto_20171212_0519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='size',
            name='size_name',
            field=models.CharField(max_length=20),
        ),
    ]