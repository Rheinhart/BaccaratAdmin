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


class AdminuserAdminuser(models.Model):
    name = models.CharField(unique=True, max_length=30)
    sex = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=64, blank=True, null=True)
    nickname = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'adminuser_adminuser'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission_id'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user_id', 'group_id'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user_id', 'permission_id'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    user = models.ForeignKey(AuthUser)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class TAgents(models.Model):
    agentcode = models.AutoField(primary_key=True)
    agentname = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    flag = models.IntegerField()
    try_type = models.IntegerField()
    create_time = models.DateTimeField()
    create_ip = models.CharField(max_length=16)

    class Meta:
        managed = False
        db_table = 't_agents'


class TBulletin(models.Model):
    bulletinid = models.AutoField(primary_key=True)
    create_time = models.DateTimeField()
    expired_time = models.DateTimeField()
    text = models.CharField(max_length=200)
    flag = models.IntegerField()

    class Meta:
        managed = False
        db_table = 't_bulletin'


class TControllerlog(models.Model):
    loginname = models.CharField(primary_key=True, max_length=16)
    action = models.CharField(max_length=64)
    action_time = models.DateTimeField()
    remark = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 't_controllerlog'


class TControllers(models.Model):
    loginname = models.CharField(primary_key=True, max_length=16)
    password = models.CharField(max_length=32)
    permit = models.IntegerField()
    flag = models.IntegerField()

    class Meta:
        managed = False
        db_table = 't_controllers'


class TCustomerTrans(models.Model):
    transid = models.AutoField(primary_key=True)
    action_time = models.DateTimeField()
    loginname = models.CharField(max_length=16)
    agentcode = models.IntegerField()
    action = models.CharField(max_length=32)
    trans_amount = models.FloatField()
    before_credit = models.FloatField()
    after_credit = models.FloatField()
    remark = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 't_customer_trans'


class TCustomers(models.Model):
    customerid = models.AutoField(primary_key=True)
    loginname = models.CharField(max_length=32)
    agentcode = models.IntegerField()
    password = models.CharField(max_length=32)
    nickname = models.CharField(max_length=32)
    flag = models.IntegerField()
    credit = models.FloatField()
    limitid = models.IntegerField()
    create_time = models.DateTimeField()
    create_ip = models.CharField(max_length=16)
    last_login_time = models.DateTimeField()
    last_login_ip = models.CharField(max_length=16)
    pwd_expired_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 't_customers'


class TOrders(models.Model):
    billno = models.AutoField(primary_key=True)
    gametype = models.CharField(max_length=16)
    loginname = models.CharField(max_length=32)
    agentcode = models.IntegerField()
    roundcode = models.CharField(max_length=16)
    videoid = models.CharField(max_length=4)
    tableid = models.CharField(max_length=4)
    seat = models.IntegerField()
    dealer = models.CharField(max_length=16)
    flag = models.IntegerField()
    playtype = models.IntegerField()
    bet_amount = models.FloatField()
    win_amount = models.FloatField(blank=True, null=True)
    valid_bet_amount = models.FloatField(blank=True, null=True)
    hashcode = models.CharField(max_length=32)
    before_credit = models.FloatField()
    after_credit = models.FloatField()
    create_time = models.DateTimeField()
    reckon_time = models.DateTimeField(blank=True, null=True)
    create_ip = models.CharField(max_length=16)

    class Meta:
        managed = False
        db_table = 't_orders'


class TPersonalLimitset(models.Model):
    limitid = models.AutoField(primary_key=True)
    playtype = models.IntegerField()
    min = models.FloatField()
    max = models.FloatField()
    flag = models.IntegerField()

    class Meta:
        managed = False
        db_table = 't_personal_limitset'


class TRecalcRounds(models.Model):
    actionid = models.AutoField(primary_key=True)
    create_time = models.DateTimeField()
    action = models.CharField(max_length=64)
    roundcode = models.CharField(max_length=16)

    class Meta:
        managed = False
        db_table = 't_recalc_rounds'


class TRounds(models.Model):
    roundcode = models.CharField(primary_key=True, max_length=16)
    gametype = models.CharField(max_length=16)
    videoid = models.CharField(max_length=4)
    dealer = models.CharField(max_length=16, blank=True, null=True)
    flag = models.IntegerField()
    cards = models.CharField(max_length=24, blank=True, null=True)
    cardnum = models.IntegerField(blank=True, null=True)
    pair = models.IntegerField(blank=True, null=True)
    bankerpoint = models.IntegerField(blank=True, null=True)
    playerpoint = models.IntegerField(blank=True, null=True)
    begintime = models.DateTimeField()
    closetime = models.DateTimeField(blank=True, null=True)
    shoecode = models.CharField(max_length=16)

    class Meta:
        managed = False
        db_table = 't_rounds'


class TTable(models.Model):
    tableid = models.CharField(primary_key=True, max_length=4)
    videoid = models.CharField(max_length=4)
    gametype = models.CharField(max_length=16)
    flag = models.IntegerField()
    limitid = models.IntegerField()
    seats = models.IntegerField()

    class Meta:
        managed = False
        db_table = 't_table'


class TTableLimitset(models.Model):
    limitid = models.AutoField(primary_key=True)
    playtype = models.IntegerField()
    min = models.FloatField()
    max = models.FloatField()
    flag = models.IntegerField()

    class Meta:
        managed = False
        db_table = 't_table_limitset'


class TVideo(models.Model):
    videoid = models.CharField(primary_key=True, max_length=4)
    gametype = models.CharField(max_length=16)
    flag = models.IntegerField()
    bettime = models.DateTimeField()
    url = models.CharField(max_length=160)

    class Meta:
        managed = False
        db_table = 't_video'
