# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-12 06:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mall', '0010_auto_20171212_0533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='goods_created',
            field=models.DateField(auto_now_add=True),
        ),
    ]
