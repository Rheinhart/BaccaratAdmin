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


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


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


class TBulletin(models.Model):
    bulletinid = models.CharField(db_column='BulletinID', verbose_name='公告id',primary_key=True, max_length=16)  # Field name made lowercase.
    create_time = models.DateField(db_column='Create_time')  # Field name made lowercase.
    expired_time = models.DateField(db_column='Expired_time')  # Field name made lowercase.
    text = models.CharField(max_length=200)
    flag = models.IntegerField()

    class Meta:
        managed = False
        db_table = 't_bulletin'


class TControllerlog(models.Model):
    loginname = models.CharField(db_column='Loginname', primary_key=True, max_length=16)  # Field name made lowercase.
    action = models.CharField(db_column='Action', max_length=64)  # Field name made lowercase.
    action_time = models.DateField(db_column='Action_time')  # Field name made lowercase.
    remark = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 't_controllerlog'


class TControllers(models.Model):
    loginname = models.CharField(db_column='Loginname', primary_key=True, max_length=16)  # Field name made lowercase.
    password = models.CharField(max_length=32)
    permit = models.IntegerField()
    flag = models.IntegerField()

    class Meta:
        managed = False
        db_table = 't_controllers'


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


class TCustomers(models.Model):
    id = models.IntegerField(primary_key=True)
    loginname = models.CharField(db_column='Loginname', max_length=32)  # Field name made lowercase.
    agentcode = models.CharField(db_column='AgentCode', max_length=16)  # Field name made lowercase.
    password = models.CharField(max_length=32)
    nickname = models.CharField(max_length=32)
    flag = models.IntegerField()
    credit = models.FloatField()
    limitid = models.IntegerField(db_column='limitID')  # Field name made lowercase.
    create_time = models.DateField(db_column='Create_time')  # Field name made lowercase.
    create_ip = models.CharField(db_column='Create_ip', max_length=16)  # Field name made lowercase.
    last_login_time = models.DateField(db_column='Last_login_time')  # Field name made lowercase.
    last_login_ip = models.CharField(db_column='Last_login_ip', max_length=16)  # Field name made lowercase.
    pwd_expired_time = models.DateField(db_column='Pwd_expired_time')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_customers'


class TOrders(models.Model):
    billno = models.CharField(max_length=16)
    gametype = models.CharField(max_length=4)
    loginname = models.CharField(max_length=32)
    agentcode = models.CharField(db_column='AgentCode', max_length=16)  # Field name made lowercase.
    roundcode = models.CharField(max_length=16)
    videoid = models.IntegerField()
    table = models.IntegerField()
    seat = models.IntegerField()
    dealer = models.CharField(max_length=16)
    flag = models.IntegerField()
    playtype = models.IntegerField()
    bet_amount = models.IntegerField()
    hashcode = models.CharField(max_length=32)
    win_amount = models.IntegerField(db_column='Win_amount')  # Field name made lowercase.
    before_credit = models.IntegerField(db_column='Before_credit')  # Field name made lowercase.
    after_credit = models.IntegerField(db_column='After_credit')  # Field name made lowercase.
    create_time = models.DateField(db_column='Create_time')  # Field name made lowercase.
    reckon_time = models.DateField(db_column='Reckon_time')  # Field name made lowercase.
    ip = models.CharField(max_length=16)

    class Meta:
        managed = False
        db_table = 't_orders'


class TPersonalLimitset(models.Model):
    limitid = models.CharField(db_column='LimitID', primary_key=True, max_length=4)  # Field name made lowercase.
    playtype = models.IntegerField(db_column='PlayType')  # Field name made lowercase.
    min = models.IntegerField(db_column='Min')  # Field name made lowercase.
    max = models.IntegerField(db_column='Max')  # Field name made lowercase.
    flag = models.IntegerField(db_column='Flag')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_personal_limitset'


class TRecalcRounds(models.Model):
    actionid = models.CharField(primary_key=True, max_length=16)
    create_time = models.DateField(db_column='Create_time')  # Field name made lowercase.
    action = models.CharField(max_length=64)
    roundcode = models.CharField(max_length=16)

    class Meta:
        managed = False
        db_table = 't_recalc_rounds'


class TRounds(models.Model):
    roundcode = models.CharField(primary_key=True, max_length=16)
    gametype = models.CharField(max_length=4)
    videoid = models.CharField(max_length=4)
    dealer = models.BigIntegerField(blank=True, null=True)
    flag = models.IntegerField()
    cards = models.CharField(max_length=24, blank=True, null=True)
    bankerpoint = models.IntegerField(blank=True, null=True)
    playerpoint = models.IntegerField(blank=True, null=True)
    begintime = models.DateField()
    closetime = models.DateField(blank=True, null=True)
    shoecode = models.CharField(max_length=16)

    class Meta:
        managed = False
        db_table = 't_rounds'


class TTable(models.Model):
    tableid = models.CharField(db_column='TableID', primary_key=True, max_length=4)  # Field name made lowercase.
    videoid = models.CharField(db_column='VideoID', max_length=4)  # Field name made lowercase.
    gametype = models.CharField(db_column='GameType', max_length=4)  # Field name made lowercase.
    flag = models.IntegerField(db_column='Flag')  # Field name made lowercase.
    limitid = models.IntegerField(db_column='LimitID')  # Field name made lowercase.
    seats = models.IntegerField()

    class Meta:
        managed = False
        db_table = 't_table'


class TTableLimitset(models.Model):
    limitid = models.CharField(db_column='LimitID', primary_key=True, max_length=4)  # Field name made lowercase.
    playtype = models.IntegerField(db_column='PlayType')  # Field name made lowercase.
    min = models.IntegerField(db_column='Min')  # Field name made lowercase.
    max = models.IntegerField(db_column='Max')  # Field name made lowercase.
    flag = models.IntegerField(db_column='Flag')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_table_limitset'


class TVideo(models.Model):
    videoid = models.CharField(db_column='VideoID', primary_key=True, max_length=4)  # Field name made lowercase.
    gametype = models.CharField(db_column='GameType', max_length=4)  # Field name made lowercase.
    flag = models.IntegerField(db_column='Flag')  # Field name made lowercase.
    bettime = models.DateField(db_column='BetTime')  # Field name made lowercase.
    url = models.CharField(db_column='URL', max_length=160)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_video'