#coding:utf8
# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals
from django.db import models
from django.contrib import admin
from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from BaccaratAdmin.tools.protobuff import bulletin_pb2,tableLimit_pb2
import datetime
import requests
import os
import json
from django.db.models.signals import post_save
from django.dispatch import receiver
from BaccaratAdmin.tools.fireflymem.memopr import *

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

@receiver(post_save, sender=TBulletin)
def pushBulletinToGameSer(sender,instance,**argvs):
        """push bulletin to the gameserver after which saved into the database
        """
        command = 20037
        config = json.load(open(path))
        url = config['Server']['url']
        port = config['Server']['port']
        return requests.get('%s:%s/bulletin?command=%s'%(url,port,command))

@admin.register(TBulletin)
class TBulletinAdmin(admin.ModelAdmin):

    list_display = ('bulletinid','text','create_time','expired_time','flag')
    search_fields = ('bulletinid','flag')

    def save_model(self, request, obj, form, change):
        obj.save()
        #obj.pushBulletinToGameSer()


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

@receiver(post_save, sender=TTableLimitset)
def pushTableLimitToGameSer(instance,**argvs):
        """push TableLimit message to the gameserver after which saved into the database
        """
        mytableLimit = tableLimit_pb2.tableLimit()
        mytableLimit.limitid = instance.limitid
        mytableLimit.playtype = instance.playtype
        mytableLimit.min = instance.min
        mytableLimit.max = instance.max
        mytableLimit.flag = instance.flag

        config = json.load(open(path))
        url = config['Server']['url']
        port = config['Server']['port']

        return requests.post('%s:%s'%(url,port),mytableLimit.SerializeToString())

@admin.register(TTableLimitset)
class TTableLimitsetAdmin(admin.ModelAdmin):

    list_display = ('limitid','playtype','min_cents','max_cents','flag')


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

@admin.register(TPersonalLimitset)
class TPersonalLimitsetAdmin(admin.ModelAdmin):

    list_display = ('limitid','playtype','min_cents','max_cents','flag')
    search_fields = ('limitid','playtype','min_cents','max_cents','flag')


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


@admin.register(TCustomers)
class TCustomersAdmin(admin.ModelAdmin):
    list_display = ('loginname','nickname','credit_cents','limitid','create_time','create_ip','last_login_time','last_login_ip','pwd_expired_time','flag')


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
    ip = models.CharField(max_length=16)

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


@admin.register(TRounds)
class TRoundAdmin(admin.ModelAdmin):

    list_display = ('roundcode','gametype','videoid','dealer','cards','begintime','closetime','shoecode')

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
    videoid = models.CharField(db_column='VideoID', verbose_name= u'视频ID',primary_key=True, max_length=4)  # Field name made lowercase.
    gametype = models.CharField(db_column='GameType', verbose_name= u'游戏类型', max_length=16)  # Field name made lowercase.
    flag = models.IntegerField(db_column='Flag',verbose_name= u'是否禁用',choices=FLAG,default=0)
    bettime = models.IntegerField(db_column='BetTime',verbose_name= u'下注倒计时(s)')  # Field name made lowercase.
    url = models.URLField(db_column='URL', max_length=160)  # Field name made lowercase.

    def change_Video(self):
        mdata = {'videoid':self.videoid,'url':self.url,'flag':self.flag,'bettime':self.bettime,'gametype':self.gametype}
        changeVideotoMem(mdata)
    def add_Video(self):
        mdata = {'videoid':self.videoid,'url':self.url,'flag':self.flag,'bettime':self.bettime,'gametype':self.gametype}
        addVideotoMem(mdata)

    def __unicode__(self):
        return '视频信息 %s' %self.videoid

    class Meta:
        managed = False
        db_table = 't_video'
        verbose_name =  u'视频信息表'
        verbose_name_plural =  u'视频信息表'


@admin.register(TVideo)
class TVideoAdmin(admin.ModelAdmin):

    list_display = ('videoid','gametype','bettime','url','flag')
    search_fields = ('videoid','gametype','bettime','url','flag')
    #readonly_fields = ('videoid',)


    def get_actions(self, request):
        """只允许特定管理者有删除视频权限"""
        actions = super(TVideoAdmin, self).get_actions(request)
        if not request.user.is_superuser or request.user.username.upper() != 'ADMIN':
            if 'delete_selected' in actions:
                del actions['delete_selected']
        return actions

    #def mem_refresh(self, request, queryset):
    #    updateVideoMemToDb()
    #mem_refresh.short_description = u'更新所有的视频信息表'

    def get_readonly_fields(self,request,obj=None):
        return self.readonly_fields

    def changelist_view(self, request, extra_context=None):
        """
        The 'change list' admin view for this model.
        """
        updateVideoMemToDb()
        get_readonly_fields=('videoid')
        return super(TVideoAdmin, self).changelist_view(request,extra_context=extra_context)

    def save_model(self, request, obj, form, change):
        if change: #change
            #obj_old = self.model.objects.get(pk=obj.pk)
            print 'change: Mem'
            obj.change_Video()
        else: #add
            print 'add:Db to Mem'
            obj.save()
            updateVideoDbtoMem()

        #obj.save()


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

@admin.register(TTable)
class TTableAdmin(admin.ModelAdmin):

    list_display = ('tableid','videoid','gametype','limitid','seats','flag','get_video_url')
    search_fields = ('tableid','videoid','gametype','limitid')

    def get_video_url(self,obj):
        return obj.videoid.url
    get_video_url.short_description = u'视频URL'



#class TAgents(models.Model):
    # agentcode = models.CharField(db_column='AgentCode', primary_key=True, max_length=16)  # Field name made lowercase.
    # agentname = models.CharField(db_column='AgentName', max_length=32)  # Field name made lowercase.
    # password = models.CharField(max_length=32)
    # flag = models.IntegerField()
    # trytype = models.IntegerField(db_column='tryType')  # Field name made lowercase.
    # create_time = models.DateField(db_column='Create_time')  # Field name made lowercase.
    # create_ip = models.CharField(db_column='Create_ip', max_length=16)  # Field name made lowercase.
    #
    # class Meta:
    #     managed = False
    #     db_table = 't_agents'