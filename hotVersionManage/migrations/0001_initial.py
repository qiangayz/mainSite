# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-14 15:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='VersionRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('formnum', models.CharField(max_length=32)),
                ('versionname', models.CharField(max_length=32)),
                ('commituser', models.CharField(max_length=64)),
                ('committime', models.CharField(max_length=64, null=True)),
                ('testtime', models.CharField(max_length=64, null=True)),
                ('ommb', models.CharField(max_length=64, null=True)),
                ('subnet', models.CharField(max_length=64, null=True)),
                ('neid', models.CharField(max_length=64, null=True)),
                ('iscloudtest', models.CharField(max_length=64, null=True)),
                ('cloudtestresult', models.CharField(max_length=64, null=True)),
            ],
        ),
    ]
