# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-08-10 23:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('ultima_modificacao', models.DateTimeField(auto_now=True)),
                ('autor', models.CharField(blank=True, max_length=64, null=True)),
                ('texto', models.TextField(blank=True, null=True)),
                ('titulo', models.TextField(unique=True)),
            ],
        ),
    ]
