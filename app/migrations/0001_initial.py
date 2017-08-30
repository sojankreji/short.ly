# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-30 19:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MiniUrl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(unique=True, verbose_name='URL a reduire')),
                ('code', models.CharField(max_length=6, unique=True)),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date:')),
                ('pseudo', models.CharField(blank=True, max_length=255, null=True)),
                ('nb_acces', models.IntegerField(default=0, verbose_name="Nombre d'acces a l'URL")),
            ],
            options={
                'verbose_name_plural': 'Mini URLS',
                'verbose_name': 'Mini URL',
            },
        ),
    ]