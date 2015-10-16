from django.test import TestCase

# Create your tests here.
from BaccaratAdmin.livecontroll.views import BulletinOpr
from BaccaratAdmin.livecontroll.models import TBulletin
#p=TControllers(loginname = 'thomas', password = '123456', permit=1,flag=0)
#p.save()

TBulletin.addBulletin()