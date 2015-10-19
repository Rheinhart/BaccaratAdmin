from django.shortcuts import render

# Create your views here.
from BaccaratAdmin.toolfunc import checklogin,checkMD5,checkSecurity,MakeLoginArgs,MakeSecurityURL
from BaccaratAdmin.livecontroll.models import TCustomers,TRounds,TTable,TTableLimitset,TVideo,TPersonalLimitset,TOrders
from BaccaratAdmin.livecontroll.controll import BulletinOper
from BaccaratAdmin.errormsg import  *
from django.shortcuts import HttpResponse,render_to_response
import json
import datetime


BOpr = BulletinOper.BulletinOper.addBulletin()
