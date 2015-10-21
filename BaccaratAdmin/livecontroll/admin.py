from django.contrib import admin

# Register your models here.
from BaccaratAdmin.tools.protobuff import login_pb2
import requests
import os
import json
from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in

path =os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__),os.path.pardir)),'config.json')

@receiver(user_logged_in)
def pushLoginMessageToGameSer(**argvs):
        """push message to the gameserver when login
           code: 0x00050002
        """
        message = {'code':'0x00050002','message':'Manager login success!'}

        config = json.load(open(path))
        url = config['Server']['url']
        port = config['Server']['port']

        return requests.post('%s:%s'%(url,port),message)