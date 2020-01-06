# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-01-03 04:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('instaApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='profile',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='instaApp.Profile'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image',
            name='ilikes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='image',
            name='iname',
            field=models.CharField(default='Post', max_length=30),
        ),
    ]