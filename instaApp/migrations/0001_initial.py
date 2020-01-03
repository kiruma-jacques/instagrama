# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-01-02 16:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import pyuploadcare.dj.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', pyuploadcare.dj.models.ImageField()),
                ('iname', models.CharField(max_length=30)),
                ('icaption', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('avatar', pyuploadcare.dj.models.ImageField()),
                ('bio', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='image',
            name='iprofile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instaApp.Profile'),
        ),
        migrations.AddField(
            model_name='comments',
            name='image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instaApp.Image'),
        ),
    ]