#coding:utf8
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime
import requests
import os
import json
from BaccaratAdmin.livecontroll.memopr import Memmode_Operation

path =os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__),os.path.pardir)),'config.json')

class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'

class TBulletin(models.Model):
    """公告操作相关
    """
    FLAG = ((0,u'启用'),(1,u'禁用'),)

    bulletinid = models.AutoField(verbose_name= u'公告id',max_length=11,primary_key=True)
    create_time = models.DateTimeField(verbose_name= u'创建时间',default=datetime.datetime.now)
    expired_time = models.DateTimeField(verbose_name= u'到期时间')
    text = models.TextField(max_length=200,verbose_name= u'公告内容')
    flag = models.IntegerField(verbose_name= u'是否禁用',choices=FLAG,default=0)   #0:启用,1:禁用

    def pushBulletinToGameSer(self):
        """push bulletin to the gameserver after which saved into the database
        """
        mybulletin = bulletin_pb2.bulletinResponse()
        mybulletin.beginTime = self.create_time.strftime("%Y-%m-%d %H:%M:%S")
        mybulletin.endTime = self.expired_time.strftime("%Y-%m-%d %H:%M:%S")
        mybulletin.text = self.text

        config = json.load(open(path))
        url = config['Server']['url']
        port = config['Server']['port']

        return requests.post('%s:%s'%(url,port),mybulletin.SerializeToString())

    def __unicode__(self):
        '''
        '''
        return '公告 %s' %self.bulletinid

    class Meta:
        managed = False
        db_table = 't_bulletin'
        verbose_name = u'公告信息'
        verbose_name_plural = u'公告信息'


class TTableLimitset(models.Model):

    FLAG = ((0,u'启用'),(1,u'禁用'),)

    limitid = models.CharField(db_column='LimitID',verbose_name= u'盘口id', primary_key=True, max_length=4)  # Field name made lowercase.
    playtype = models.IntegerField(db_column='PlayType',verbose_name= u'玩法',validators=[MinValueValidator(0), MaxValueValidator(9999)])  # Field name made lowercase.
    min_cents = models.FloatField(db_column='Min_Cents',verbose_name= u'最小下注额度')  # Field name made lowercase.
    max_cents = models.FloatField(db_column='Max_Cents',verbose_name= u'最大下注额度')  # Field name made lowercase.
    flag = models.IntegerField(db_column='Flag',verbose_name= u'是否禁用',choices=FLAG,default=0)  # Field name made lowercase.

    def __unicode__(self):
        '''
        '''
        return  u'桌台限红 %s' %self.tableid

    class Meta:
        managed = False
        db_table = 't_table_limitset'
        verbose_name =  u'桌台限红表'
        verbose_name_plural =  u'桌台限红表'


class TPersonalLimitset(models.Model):

    FLAG = ((0,u'启用'),(1,u'禁用'),)

    limitid = models.CharField(db_column='LimitID',verbose_name= u'盘口id',primary_key=True,max_length=11)  # Field name made lowercase.
    playtype = models.IntegerField(db_column='PlayType',verbose_name= u'玩法',validators=[MinValueValidator(0), MaxValueValidator(9999)])  # Field name made lowercase.
    min_cents = models.FloatField(db_column='Min_Cents', verbose_name= u'最小下注额度')  # Field name made lowercase.
    max_cents = models.FloatField(db_column='Max_Cents', verbose_name= u'最大下注额度')  # Field name made lowercase.
    flag = models.IntegerField(db_column='Flag',verbose_name = u'是否禁用',choices=FLAG,default=0)  # Field name made lowercase.

    def __unicode__(self):
        '''
        '''
        return  u'个人限红 %s' %self.limitid

    class Meta:
        managed = False
        db_table = 't_personal_limitset'
        verbose_name =  u'个人限红表'
        verbose_name_plural =  u'个人限红表'


class TCustomers(models.Model):

    FLAG = ((0,u'启用'),(1,u'禁用'),)

    loginname = models.CharField(db_column='Loginname',verbose_name= u'登录名', max_length=32,primary_key=True)  # Field name made lowercase.
    agentcode = models.IntegerField(db_column='AgentCode',verbose_name= u'代理CODE',validators=[MinValueValidator(0), MaxValueValidator(9999)])  # Field name made lowercase.
    password = models.CharField(max_length=32,verbose_name= u'密码')
    nickname = models.CharField(max_length=32,verbose_name= u'昵称')
    flag = models.IntegerField(db_column='Flag',verbose_name= u'是否禁用',choices=FLAG,default=0)
    credit_cents = models.FloatField(db_column='Credit_cents')
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

    transid = models.CharField(primary_key=True, max_length=16)
    actoin_time = models.DateField(db_column='Actoin_time')  # Field name made lowercase.
    loginname = models.CharField(max_length=16)
    agentcode = models.CharField(db_column='AgentCode', max_length=16)  # Field name made lowercase.
    action = models.CharField(max_length=32)
    trans_amount = models.IntegerField(db_column='Trans_amount')  # Field name made lowercase.
    before_credit = models.IntegerField(db_column='Before_credit')  # Field name made lowercase.
    after_credit = models.IntegerField(db_column='After_credit')  # Field name made lowercase.
    remark = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 't_customer_trans'


class TOrders(models.Model):

    FLAG = ((0,u'启用'),(1,u'禁用'),)

    billno = models.CharField(max_length=16)
    gametype = models.CharField(max_length=4)
    loginname = models.CharField(max_length=32)
    agentcode = models.CharField(db_column='AgentCode', max_length=16)  # Field name made lowercase.
    roundcode = models.CharField(max_length=16)
    videoid = models.IntegerField()
    table = models.IntegerField()
    seat = models.IntegerField()
    dealer = models.CharField(max_length=16)
    flag = models.IntegerField(db_column='Flag',verbose_name= u'是否禁用',choices=FLAG,default=0)
    playtype = models.IntegerField()
    bet_amount = models.IntegerField()
    hashcode = models.CharField(max_length=32)
    win_amount = models.IntegerField(db_column='Win_amount')  # Field name made lowercase.
    before_credit = models.IntegerField(db_column='Before_credit')  # Field name made lowercase.
    after_credit = models.IntegerField(db_column='After_credit')  # Field name made lowercase.
    create_time = models.DateTimeField(db_column='Create_time',verbose_name= u'创建时间',default=datetime.datetime.now)  # Field name made lowercase.
    reckon_time = models.DateTimeField(db_column='Reckon_time')  # Field name made lowercase.
    ip = models.GenericIPAddressField(db_column='ip',verbose_name= u'IP', max_length=16)

    class Meta:
        managed = False
        db_table = 't_orders'


class TRounds(models.Model):

    FLAG = ((0,u'启用'),(1,u'禁用'),)

    roundcode = models.CharField(primary_key=True, max_length=16)
    gametype = models.CharField(max_length=4,verbose_name= u'玩法')
    videoid = models.CharField(max_length=4,verbose_name= u'视频id')
    dealer = models.BigIntegerField(blank=True, null=True , verbose_name= u'荷官')
    flag = models.IntegerField(db_column= u'Flag',verbose_name= u'是否禁用',choices=FLAG,default=0)
    cards = models.CharField(max_length=24, blank=True, null=True)
    bankerpoint = models.IntegerField(blank=True, null=True,verbose_name= u'庄家')
    playerpoint = models.IntegerField(blank=True, null=True,verbose_name= u'闲家')
    begintime = models.DateTimeField(verbose_name= u'开始时间',default=datetime.datetime.now)
    closetime = models.DateTimeField(blank=True, null=True,verbose_name= u'结束时间')
    shoecode = models.CharField(max_length=16,verbose_name='靴号')

    class Meta:
        managed = False
        db_table = 't_rounds'
        verbose_name =  u'游戏局表'
        verbose_name_plural =  u'游戏局表'


class TRecalcRounds(models.Model):


    actionid = models.CharField(primary_key=True, max_length=16)
    create_time = models.DateTimeField(db_column='Create_time',verbose_name= u'创建时间',default=datetime.datetime.now)  # Field name made lowercase.
    action = models.CharField(max_length=64)
    roundcode = models.CharField(max_length=16)

    class Meta:
        managed = False
        db_table = 't_recalc_rounds'

class TVideo(models.Model):

    FLAG = ((0,u'启用'),(1,u'禁用'),)
    GAMETYPE = (('BJL',u'百家乐'),('DDZ',u'斗地主'))
    videoid = models.CharField(db_column='VideoID', verbose_name= u'视频ID',primary_key=True, max_length=4)  # Field name made lowercase.
    gametype = models.CharField(db_column='GameType', verbose_name= u'游戏类型', max_length=16,choices=GAMETYPE,default='BJL')  # Field name made lowercase.
    flag = models.IntegerField(db_column='Flag',verbose_name= u'是否禁用',choices=FLAG,default=0)
    bettime = models.IntegerField(db_column='BetTime',verbose_name= u'下注倒计时(秒)')  # Field name made lowercase.
    url = models.URLField(db_column='URL', max_length=160)  # Field name made lowercase.

    memopr=Memmode_Operation()

    def change_video(self):
        mdata = {'videoid':self.videoid,'url':self.url,'flag':self.flag,'bettime':self.bettime,'gametype':self.gametype}
        self.memopr.changeVideotoMem(mdata)

    def add_video(self):
        self.memopr.updateVideoDbtoMem()

    def __unicode__(self):
        return '视频信息 %s' %self.videoid

    class Meta:
        managed = False
        db_table = 't_video'
        verbose_name =  u'视频信息表'
        verbose_name_plural =  u'视频信息表'


class TTable(models.Model):
    """桌台操作相关"""

    FLAG = ((0,u'启用'),(1,u'禁用'),)

    tableid = models.CharField(db_column='TableID',verbose_name= u'桌台id', primary_key=True, max_length=4)  # Field name made lowercase.
    #videoid = models.CharField(db_column='VideoID',verbose_name= u'视频id', max_length=4)  # Field name made lowercase.
    videoid = models.ForeignKey(TVideo,db_column= 'VideoID',verbose_name=u'视频id')
    gametype = models.CharField(db_column='GameType',verbose_name= u'玩法', max_length=16)  # Field name made lowercase.
    limitid = models.CharField(db_column='LimitID',verbose_name= u'限红id',max_length=4)  # Field name made lowercase.
    seats = models.IntegerField(db_column='Seats',validators=[MinValueValidator(0), MaxValueValidator(9999)],verbose_name= u'座位数')
    flag = models.IntegerField(db_column='Flag',verbose_name= u'是否禁用',choices=FLAG,default=0)  # Field name made lowercase.

    def __unicode__(self):
        '''
        '''
        return self.tableid

    class Meta:
        managed = False
        db_table = 't_table'
        verbose_name = u'桌台信息'
        verbose_name_plural = u'桌台信息'




