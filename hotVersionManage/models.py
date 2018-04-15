# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class UserInfo(models.Model):
    username=models.CharField(max_length=32)
    password=models.CharField(max_length=64)

class VersionRecord(models.Model):
    formnum=models.CharField(max_length=32)
    versionname=models.CharField(max_length=32)
    commituser=models.CharField(max_length=64)
    otherinfo=models.CharField(max_length=128,null=True)
    committime=models.CharField(max_length=64,null=True)
    verpath=models.CharField(max_length=64,null=True)
    testtime=models.CharField(max_length=64,null=True)
    ommb=models.CharField(max_length=64,null=True)
    subnet=models.CharField(max_length=64,null=True)
    neid=models.CharField(max_length=64,null=True)
    iscloudtest=models.CharField(max_length=64,null=True)
    cloudtestresult=models.CharField(max_length=64,null=True)

class VersionRunInfo(models.Model):
    versionname = models.CharField(max_length=32)
    versionpath = models.CharField(max_length=64)
    ispull = models.CharField(max_length=32,null=True)
    isrun = models.CharField(max_length=32,null=True)
    iscloudtest = models.CharField(max_length=32,null=True)
    iscloudtestrun = models.CharField(max_length=32,null=True)
    cloudtest_result = models.CharField(max_length=32,null=True)

