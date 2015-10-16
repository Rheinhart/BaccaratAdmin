from django.shortcuts import render

# Create your views here.
from BaccaratAdmin.toolfunc import checklogin,checkMD5,checkSecurity,MakeLoginArgs,MakeSecurityURL
from BaccaratAdmin.livecontroll.models import TBulletin
from BaccaratAdmin.errormsg import  *
from django.shortcuts import HttpResponse,render_to_response
import json
import datetime

class BulletinOpr(object):

    def getBulletinById():
        pass

    def addBulletin(self):

        #bulletinId = request.REQUEST['bulletinid']
        bulletinid = 0000125
        create_time = '2015-10-15 23:59:59'
        expired_time = '2015-10-16 12:22:13'
        text = 'I am a large One'
        flag = 1

        myBulletin=TBulletin(bulletinid,create_time,expired_time,text,flag)
        myBulletin.save()

        return myBulletin





