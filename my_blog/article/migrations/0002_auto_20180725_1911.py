# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-25 11:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myarticle',
            name='auditing',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='myarticle',
            name='is_show',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='myarticle',
            name='recommend',
            field=models.BooleanField(default=0),
        ),
    ]
