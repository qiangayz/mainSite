# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import HttpResponse
from hotVersionManage import models
import threading
import os
import time

def index(request):
    return  render(request,'index.html')

def login(request):
    error_msg1=''
    error_msg2=''
    if request.method == "POST":
        u = request.POST.get('username',None)
        p = request.POST.get('password',None)
        if len(u)==0 and len(p)==0:
            error_msg1 = 'username is null'
            error_msg2 = 'password is null'
        elif len(u) == 0:
            error_msg1 = 'username is null'
        else :
            error_msg2 = 'password is null'
        obj=models.UserInfo.objects.filter(username=u,password=p).first()
        if obj :
             return redirect('/index/')
        else:
             return render(request, 'login.html',{'msg1':error_msg1,'msg2':error_msg2})
    return render(request,'login.html')

def versionCommit(request):
    msg=[]
    msg1='none'
    if request.method == "POST":
        commit_user=request.POST.get('commituser',None)
        OMMBid=request.POST.get('OMMBid', None)
        subid=request.POST.get('subid', None)
        neid=request.POST.get('neid', None)
        parent_path=request.POST.get('parent_path', None)
        cloudtest_tag=request.POST.get('cloudtesttag', None)
        other_data=request.POST.get('otherdata',None)
        cloudtest_tag = 1 if cloudtest_tag else 0
        obj = request.FILES.get('versionfile',None)
        filename=obj.name
        file_path = os.path.join(r'static/hotVersion', obj.name)
        f = open(file_path,mode='wb' )
        for i in obj.chunks():
            f.write(i)
        f.close()
        commit_time=str(time.strftime("%Y-%m-%d %H:%M:%S"))
        form_num = 'H'+str(time.strftime("%Y%m%d%H%M%S"))

        models.VersionRecord.objects.create(formnum=form_num,versionname=filename,commituser=commit_user,otherinfo=other_data,committime=commit_time,verpath=file_path)
        msg1 = 'block'
        t1 = threading.Thread(target=run, args=( filename,file_path,parent_path,OMMBid, subid, neid, cloudtest_tag))
        t1.start()
        msg = [form_num, commit_time, commit_user, OMMBid, subid, neid, parent_path, filename, cloudtest_tag,
               other_data]
        return  render(request,'Commit.html',
               {'msg':msg,'msg1':msg1})
    return  render(request,'Commit.html',{'msg':msg,'msg1':msg1})

def versionManage(request):
    data=[]
    obj=models.VersionRecord.objects.all()
    for i in obj:
        data.append(i.versionname)

    return render(request,'Manage.html',{'versionlist':data})

def run(*args):
    for i in args:
        print '--->',i
        time.sleep(5)