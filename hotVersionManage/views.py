# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import HttpResponse
from hotVersionManage import models
import threading
import os
import time

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
        if obj and u == 'admin':
             return redirect('/versionManage/')
        elif obj:
             return redirect('/versionCommit/')
        else:
             return render(request, 'login.html',{'msg1':error_msg1,'msg2':error_msg2})
    return render(request,'login.html')

def versionCommit(request):
    if request.method == "POST":
        commit_user=request.POST.get('commituser',None)
        other_data=request.POST.get('otherdata',None)
        cloudtest_tag=request.POST.get('cloudtesttag',None)
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
        return  render(request,'commitsuccess.html',
               {'msg1':commit_user,
                'msg2':other_data,
                'msg3':cloudtest_tag,
                'msg4':filename,
                'msg5':file_path
                })
    return  render(request,'Commit.html')

def versionManage(request):
    print request.method
    successmsg = ''
    if request.method=="POST":
        vernum=request.POST.get('VerNum', None)
        OMMBid=request.POST.get('OMMBid', None)
        subid=request.POST.get('subid', None)
        neid=request.POST.get('neid', None)
        cloudtesttag=request.POST.get('cloudtesttag', None)
        obj = models.VersionRecord.objects.filter(versionname=vernum).first()
        t1 = threading.Thread(target=run, args=(vernum,vernum,OMMBid,subid,neid,cloudtesttag,obj.verpath))
        t1.start()
        successmsg = '提交成功!!'
    data=[]
    obj=models.VersionRecord.objects.all()
    for i in obj:
        data.append(i.versionname)

    return render(request,'Manage.html',{'versionlist':data,'successmsg':successmsg})

def run(*args):
    for i in args:
        print '--->',i
        time.sleep(5)