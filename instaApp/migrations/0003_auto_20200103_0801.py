# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-01-03 08:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instaApp', '0002_auto_20200103_0437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='iname',
            field=models.CharField(max_length=30),
        ),
    ]