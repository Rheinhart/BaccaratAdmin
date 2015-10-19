# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TBulletin',
            fields=[
                ('bulletinid', models.AutoField(max_length=11, serialize=False, verbose_name='\u516c\u544aid', primary_key=True)),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('expired_time', models.DateTimeField(verbose_name='\u5230\u671f\u65f6\u95f4')),
                ('text', models.TextField(max_length=200, verbose_name='\u516c\u544a\u5185\u5bb9')),
                ('flag', models.IntegerField(default=0, verbose_name='\u662f\u5426\u7981\u7528', choices=[(0, '\u542f\u7528'), (1, '\u7981\u7528')])),
            ],
            options={
                'verbose_name': '\u516c\u544a\u4fe1\u606f',
                'db_table': 't_bulletin',
                'managed': False,
                'verbose_name_plural': '\u516c\u544a\u4fe1\u606f',
                'permissions': (('add_bulletin', 'Can add a bulletin'), ('del_bulletin', 'Can delete bulletins'), ('edit_discussion', 'Can edit bulletins')),
            },
        ),
        migrations.CreateModel(
            name='TCustomers',
            fields=[
                ('customerid', models.IntegerField(serialize=False, verbose_name='\u7528\u6237ID', primary_key=True)),
                ('loginname', models.CharField(max_length=32, verbose_name='\u767b\u5f55\u540d', db_column='Loginname')),
                ('agentcode', models.CharField(max_length=16, verbose_name='\u4ee3\u7406CODE', db_column='AgentCode')),
                ('password', models.CharField(max_length=32, verbose_name='\u5bc6\u7801')),
                ('nickname', models.CharField(max_length=32, verbose_name='\u6635\u79f0')),
                ('flag', models.IntegerField(default=0, verbose_name='\u662f\u5426\u7981\u7528', db_column='Flag', choices=[(0, '\u542f\u7528'), (1, '\u7981\u7528')])),
                ('credit', models.FloatField()),
                ('limitid', models.IntegerField(verbose_name='\u4e2a\u4eba\u76d8\u53e3ID', db_column='limitID')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u521b\u5efa\u65f6\u95f4', db_column='Create_time')),
                ('create_ip', models.GenericIPAddressField(db_column='Create_ip')),
                ('last_login_time', models.DateTimeField(verbose_name='\u6700\u540e\u4e00\u6b21\u767b\u5f55\u65f6\u95f4', db_column='Last_login_time')),
                ('last_login_ip', models.GenericIPAddressField(verbose_name='\u6700\u6709\u4e00\u6b21\u767b\u5f55IP', db_column='Last_login_ip')),
                ('pwd_expired_time', models.DateTimeField(verbose_name='\u5bc6\u7801\u5931\u6548\u65f6\u95f4', db_column='Pwd_expired_time')),
            ],
            options={
                'verbose_name': '\u7528\u6237\u4fe1\u606f\u8868',
                'db_table': 't_customers',
                'managed': False,
                'verbose_name_plural': '\u7528\u6237\u4fe1\u606f\u8868',
            },
        ),
        migrations.CreateModel(
            name='TCustomerTrans',
            fields=[
                ('transid', models.CharField(max_length=16, serialize=False, primary_key=True)),
                ('actoin_time', models.DateField(db_column='Actoin_time')),
                ('loginname', models.CharField(max_length=16)),
                ('agentcode', models.CharField(max_length=16, db_column='AgentCode')),
                ('action', models.CharField(max_length=32)),
                ('trans_amount', models.IntegerField(db_column='Trans_amount')),
                ('before_credit', models.IntegerField(db_column='Before_credit')),
                ('after_credit', models.IntegerField(db_column='After_credit')),
                ('remark', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 't_customer_trans',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TOrders',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('billno', models.CharField(max_length=16)),
                ('gametype', models.CharField(max_length=4)),
                ('loginname', models.CharField(max_length=32)),
                ('agentcode', models.CharField(max_length=16, db_column='AgentCode')),
                ('roundcode', models.CharField(max_length=16)),
                ('videoid', models.IntegerField()),
                ('table', models.IntegerField()),
                ('seat', models.IntegerField()),
                ('dealer', models.CharField(max_length=16)),
                ('flag', models.IntegerField(default=0, verbose_name='\u662f\u5426\u7981\u7528', db_column='Flag', choices=[(0, '\u542f\u7528'), (1, '\u7981\u7528')])),
                ('playtype', models.IntegerField()),
                ('bet_amount', models.IntegerField()),
                ('hashcode', models.CharField(max_length=32)),
                ('win_amount', models.IntegerField(db_column='Win_amount')),
                ('before_credit', models.IntegerField(db_column='Before_credit')),
                ('after_credit', models.IntegerField(db_column='After_credit')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u521b\u5efa\u65f6\u95f4', db_column='Create_time')),
                ('reckon_time', models.DateTimeField(db_column='Reckon_time')),
                ('ip', models.CharField(max_length=16)),
            ],
            options={
                'db_table': 't_orders',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TPersonalLimitset',
            fields=[
                ('limitid', models.IntegerField(serialize=False, verbose_name='\u76d8\u53e3id', primary_key=True, db_column='LimitID')),
                ('playtype', models.IntegerField(verbose_name='\u73a9\u6cd5', db_column='PlayType', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(9999)])),
                ('min', models.FloatField(verbose_name='\u6700\u5c0f\u4e0b\u6ce8\u989d\u5ea6', db_column='Min')),
                ('max', models.FloatField(verbose_name='\u6700\u5927\u4e0b\u6ce8\u989d\u5ea6', db_column='Max')),
                ('flag', models.IntegerField(default=0, verbose_name='\u662f\u5426\u7981\u7528', db_column='Flag', choices=[(0, '\u542f\u7528'), (1, '\u7981\u7528')])),
            ],
            options={
                'verbose_name': '\u4e2a\u4eba\u9650\u7ea2\u8868',
                'db_table': 't_personal_limitset',
                'managed': False,
                'verbose_name_plural': '\u4e2a\u4eba\u9650\u7ea2\u8868',
            },
        ),
        migrations.CreateModel(
            name='TRecalcRounds',
            fields=[
                ('actionid', models.CharField(max_length=16, serialize=False, primary_key=True)),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u521b\u5efa\u65f6\u95f4', db_column='Create_time')),
                ('action', models.CharField(max_length=64)),
                ('roundcode', models.CharField(max_length=16)),
            ],
            options={
                'db_table': 't_recalc_rounds',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TRounds',
            fields=[
                ('roundcode', models.CharField(max_length=16, serialize=False, primary_key=True)),
                ('gametype', models.CharField(max_length=4, verbose_name='\u73a9\u6cd5')),
                ('videoid', models.CharField(max_length=4, verbose_name='\u89c6\u9891id')),
                ('dealer', models.BigIntegerField(null=True, verbose_name='\u8377\u5b98', blank=True)),
                ('flag', models.IntegerField(default=0, verbose_name='\u662f\u5426\u7981\u7528', db_column='Flag', choices=[(0, '\u542f\u7528'), (1, '\u7981\u7528')])),
                ('cards', models.CharField(max_length=24, null=True, blank=True)),
                ('bankerpoint', models.IntegerField(null=True, verbose_name='\u5e84\u5bb6', blank=True)),
                ('playerpoint', models.IntegerField(null=True, verbose_name='\u95f2\u5bb6', blank=True)),
                ('begintime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u5f00\u59cb\u65f6\u95f4')),
                ('closetime', models.DateTimeField(null=True, verbose_name='\u7ed3\u675f\u65f6\u95f4', blank=True)),
                ('shoecode', models.CharField(max_length=16, verbose_name='\u9774\u53f7')),
            ],
            options={
                'verbose_name': '\u6e38\u620f\u5c40\u8868',
                'db_table': 't_rounds',
                'managed': False,
                'verbose_name_plural': '\u6e38\u620f\u5c40\u8868',
            },
        ),
        migrations.CreateModel(
            name='TTable',
            fields=[
                ('tableid', models.CharField(max_length=4, serialize=False, verbose_name='\u684c\u53f0id', primary_key=True, db_column='TableID')),
                ('videoid', models.CharField(max_length=4, verbose_name='\u89c6\u9891id', db_column='VideoID')),
                ('gametype', models.CharField(max_length=16, verbose_name='\u73a9\u6cd5', db_column='GameType')),
                ('limitid', models.IntegerField(verbose_name='\u9650\u7ea2id', db_column='LimitID', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(9999)])),
                ('seats', models.IntegerField(verbose_name='\u5ea7\u4f4d\u6570', db_column='Seats', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(9999)])),
                ('flag', models.IntegerField(default=0, verbose_name='\u662f\u5426\u7981\u7528', db_column='Flag', choices=[(0, '\u542f\u7528'), (1, '\u7981\u7528')])),
            ],
            options={
                'verbose_name': '\u684c\u53f0\u4fe1\u606f',
                'db_table': 't_table',
                'managed': False,
                'verbose_name_plural': '\u684c\u53f0\u4fe1\u606f',
            },
        ),
        migrations.CreateModel(
            name='TTableLimitset',
            fields=[
                ('limitid', models.CharField(max_length=11, serialize=False, verbose_name='\u76d8\u53e3id', primary_key=True, db_column='LimitID')),
                ('playtype', models.IntegerField(verbose_name='\u73a9\u6cd5', db_column='PlayType', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(9999)])),
                ('min', models.FloatField(verbose_name='\u6700\u5c0f\u4e0b\u6ce8\u989d\u5ea6', db_column='Min')),
                ('max', models.FloatField(verbose_name='\u6700\u5927\u4e0b\u6ce8\u989d\u5ea6', db_column='Max')),
                ('flag', models.IntegerField(default=0, verbose_name='\u662f\u5426\u7981\u7528', db_column='Flag', choices=[(0, '\u542f\u7528'), (1, '\u7981\u7528')])),
            ],
            options={
                'verbose_name': '\u684c\u53f0\u9650\u7ea2\u8868',
                'db_table': 't_table_limitset',
                'managed': False,
                'verbose_name_plural': '\u684c\u53f0\u9650\u7ea2\u8868',
            },
        ),
        migrations.CreateModel(
            name='TVideo',
            fields=[
                ('videoid', models.CharField(max_length=4, serialize=False, verbose_name='\u89c6\u9891ID', primary_key=True, db_column='VideoID')),
                ('gametype', models.CharField(max_length=16, verbose_name='\u6e38\u620f\u7c7b\u578b', db_column='GameType')),
                ('flag', models.IntegerField(default=0, verbose_name='\u662f\u5426\u7981\u7528', db_column='Flag', choices=[(0, '\u542f\u7528'), (1, '\u7981\u7528')])),
                ('bettime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u89c6\u9891\u5f00\u59cb\u65f6\u95f4', db_column='BetTime')),
                ('url', models.URLField(max_length=160, db_column='URL')),
            ],
            options={
                'verbose_name': '\u89c6\u9891\u4fe1\u606f\u8868',
                'db_table': 't_video',
                'managed': False,
                'verbose_name_plural': '\u89c6\u9891\u4fe1\u606f\u8868',
            },
        ),
    ]
