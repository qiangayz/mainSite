# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-15 15:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotVersionManage', '0002_auto_20180415_2112'),
    ]

    operations = [
        migrations.AddField(
            model_name='versionrecord',
            name='verpath',
            field=models.CharField(max_length=64, null=True),
        ),
    ]
