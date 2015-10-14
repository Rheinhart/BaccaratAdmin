from django.test import TestCase

# Create your tests here.
from BaccaratAdmin.livecontroll.models import TControllers

p=TControllers(loginname = 'thomas', password = '123456', permit=1,flag=0)
p.save()