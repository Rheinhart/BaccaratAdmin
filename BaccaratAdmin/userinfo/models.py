#coding:utf8
"""
@__author__ = 'Thomas'
"""
from django.db import models
import datetime

class TCustomers(models.Model):

    FLAG = ((0,u'启用'),(1,u'禁用'),)

    loginname = models.CharField(db_column='Loginname',verbose_name= u'用户名', max_length=32,primary_key=True)  # Field name made lowercase.
    agentcode = models.IntegerField(db_column='AgentCode',verbose_name= u'代理CODE')  # Field name made lowercase.
    password = models.CharField(max_length=32,verbose_name= u'密码')
    nickname = models.CharField(max_length=32,verbose_name= u'昵称')
    flag = models.IntegerField(db_column='Flag',verbose_name= u'是否禁用',choices=FLAG,default=0)
    credit_cents = models.IntegerField(db_column='Credit_cents')
    limitid = models.CharField(db_column='limitID',verbose_name= u'个人盘口ID',max_length=4)  # Field name made lowercase.
    create_time = models.DateTimeField(db_column='Create_time',verbose_name= u'创建时间',default=datetime.datetime.now)  # Field name made lowercase.
    create_ip = models.GenericIPAddressField(db_column='Create_ip', max_length=16)  # Field name made lowercase.
    last_login_time = models.DateTimeField(db_column='Last_login_time',verbose_name= u'最后一次登录时间')  # Field name made lowercase.
    last_login_ip = models.GenericIPAddressField(db_column='Last_login_ip',verbose_name= u'最有一次登录IP', max_length=16)  # Field name made lowercase.
    pwd_expired_time = models.DateTimeField(db_column='Pwd_expired_time',verbose_name= u'密码失效时间')  # Field name made lowercase.


    def __unicode__(self):
        '''
        '''
        return  u'用户 %s' %self.nickname

    class Meta:
        managed = False
        db_table = 't_customers'
        verbose_name =  u'用户信息表'
        verbose_name_plural =  u'用户信息表'


class TCustomerTrans(models.Model):

    transid = models.IntegerField(primary_key=True)
    action_time = models.DateField(db_column='Action_time')  # Field name made lowercase.
    loginname = models.CharField(max_length=16,verbose_name=u"用户名")
    agentcode = models.CharField(db_column='AgentCode',verbose_name= u'代理CODE',max_length=16)  # Field name made lowercase.
    action = models.CharField(max_length=32)
    trans_amount_cents = models.IntegerField(db_column='Trans_amount_Cents')  # Field name made lowercase.
    before_credit_cents = models.IntegerField(db_column='Before_credit_Cents')  # Field name made lowercase.
    after_credit_cents = models.IntegerField(db_column='After_credit_Cents')  # Field name made lowercase.
    remark = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 't_customer_trans'
        verbose_name =  u'用户额度记录表'
        verbose_name_plural =  u'用户额度记录表'


